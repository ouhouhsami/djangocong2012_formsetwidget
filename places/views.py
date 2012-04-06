from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from places.models import PlaceType, Place
from places.forms import PlaceTypeForm, PlaceForm
from django.forms.models import inlineformset_factory
from django.template.defaultfilters import slugify

def edit(request, placetype_slug):
    """
    Edit all Places linked to a PlaceType
    """
    # get_or_create a PlaceType (no permission required)
    place_type, created = PlaceType.objects.get_or_create(slug=placetype_slug, 
                                             defaults={'label':placetype_slug})
    # build the formset in a standard django way
    # extra=0, we deal with additionnal forms via empty_form
    PlaceFormSet = inlineformset_factory(PlaceType, Place, 
                                                       form=PlaceForm, extra=0)
    if request.method == "POST":
        form = PlaceTypeForm(request.POST, instance=place_type)
        formset = PlaceFormSet(request.POST, instance=place_type)
        # due to project scope (form is always valid), 
        # we process simultaneously form and formset validations
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
        else:
            # return below to show invalid forms if needed
            return render_to_response('places/edit.html', 
                                      {'form': form, 'formset':formset}, 
                                      context_instance=RequestContext(request))
    # if request.method is get or post succeed, we fill form and formset with
    # latest values. 
    form = PlaceTypeForm(instance=place_type)
    formset = PlaceFormSet(instance=place_type)
    # return below for request.method =! "POST" 
    return render_to_response('places/edit.html', 
                                      {'form': form, 'formset':formset, 
                                       }, 
                                      context_instance=RequestContext(request))


def read(request, placetype_slug):
    """
    View all Places linked to a PlaceType
    """
    place_type = PlaceType.objects.get(slug=placetype_slug)
    return render_to_response('places/read.html', {"place_type": place_type}, 
                                      context_instance=RequestContext(request))

def list(request):
    """
    List all PlaceTypes in the app
    """
    object_list = PlaceType.objects.all()
    if request.method == "POST":
        form = PlaceTypeForm(request.POST)
        if form.is_valid():
            label = form.cleaned_data['label']
            slug = slugify(label)
            place_type, created = PlaceType.objects.get_or_create(slug=slug,
                                             defaults={'label':label})
            return redirect('edit', placetype_slug=slug)
    form = PlaceTypeForm()
    return render_to_response('places/list.html', {'object_list': object_list, 'form':form}, 
                                      context_instance=RequestContext(request))