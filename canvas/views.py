from importlib.resources import Resource
from pyexpat import model
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required
def index(request):
    partners = KeyPartner.objects.all()
    activities = KeyActivity.objects.all()
    resources = KeyResource.objects.all()
    propositions = ValueProposition.objects.all()
    cost_structures = CostStructure.objects.all()
    customer_relationships = CustomerRelationship.objects.all()
    customers = CustomerSegment.objects.all()
    channels = Channel.objects.all()
    revenues = RevenueStream.objects.all()

    return render(request, "canvas/index.html", {
        "partners": partners,
        "activities": activities,
        "resources": resources,
        "propositions": propositions,
        "cost_structures": cost_structures,
        "customer_relationships": customer_relationships,
        "customers": customers,
        "channels": channels,
        "revenues": revenues,
    })


# Partnership.
@login_required
def addPartnership(request):
    partner = request.POST["partner"]
    form = AddPartnershipForm({"partner": partner})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deletePartnership(request, id=None):
    object = get_object_or_404(KeyPartner, id=id)
    object.delete()
    return redirect('canvas:index')


# Activities

@login_required
def addActivity(request):
    activity = request.POST["activity"]
    form = AddActivityForm({"activity": activity})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteActivity(request, id=None):
    object = get_object_or_404(KeyActivity, id=id)
    object.delete()
    return redirect('canvas:index')


# Resources.

@login_required
def addResource(request):
    resource = request.POST["resource"]
    form = AddResourceForm({"resource": resource})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteResource(request, id=None):
    object = get_object_or_404(KeyResource, id=id)
    object.delete()
    return redirect('canvas:index')

# Propositions


@login_required
def addProposition(request):
    proposition = request.POST["proposition"]
    form = AddPropositionForm({"proposition": proposition})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteProposition(request, id=None):
    object = get_object_or_404(ValueProposition, id=id)
    object.delete()
    return redirect('canvas:index')

# Customer Relationship


@login_required
def addCustomerRelationship(request):
    relationship = request.POST["relationship"]
    form = AddCustomerRelationshipForm({"relationship": relationship})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteCustomerRelationship(request, id=None):
    object = get_object_or_404(CustomerRelationship, id=id)
    object.delete()
    return redirect('canvas:index')

# Channels


@login_required
def addChannel(request):
    channel = request.POST["channel"]
    form = AddChannelForm({"channel": channel})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteChannel(request, id=None):
    object = get_object_or_404(Channel, id=id)
    object.delete()
    return redirect('canvas:index')


# Customer Segments

@login_required
def addCustomerSegment(request):
    segment = request.POST["segment"]
    form = AddCustomerSegmentForm({"segment": segment})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteCustomerSegment(request, id=None):
    object = get_object_or_404(CustomerSegment, id=id)
    object.delete()
    return redirect('canvas:index')


# Cost Structure

@login_required
def addCostStructure(request):
    structure = request.POST["structure"]
    form = AddCostStructureForm({"structure": structure})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteCostStructure(request, id=None):
    object = get_object_or_404(CostStructure, id=id)
    object.delete()
    return redirect('canvas:index')


# Revenue Streams

@login_required
def addRevenueStream(request):
    stream = request.POST["stream"]
    form = AddRevenueStreamForm({"stream": stream})
    if form.is_valid():
        form.save()
    return redirect('canvas:index')


@login_required
def deleteRevenueStream(request, id=None):
    object = get_object_or_404(RevenueStream, id=id)
    object.delete()
    return redirect('canvas:index')
