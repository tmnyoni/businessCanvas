from dataclasses import field
from django import forms
from .models import *


class AddPartnershipForm(forms.ModelForm):
    class Meta:
        model = KeyPartner
        fields = "__all__"


class AddActivityForm(forms.ModelForm):
    class Meta:
        model = KeyActivity
        fields = "__all__"


class AddResourceForm(forms.ModelForm):
    class Meta:
        model = KeyResource
        fields = "__all__"


class AddPropositionForm(forms.ModelForm):
    class Meta:
        model = ValueProposition
        fields = "__all__"


class AddCustomerRelationshipForm(forms.ModelForm):
    class Meta:
        model = CustomerRelationship
        fields = "__all__"


class AddChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = "__all__"


class AddCustomerSegmentForm(forms.ModelForm):
    class Meta:
        model = CustomerSegment
        fields = "__all__"


class AddCostStructureForm(forms.ModelForm):
    class Meta:
        model = CostStructure
        fields = "__all__"


class AddRevenueStreamForm(forms.ModelForm):
    class Meta:
        model = RevenueStream
        fields = "__all__"
