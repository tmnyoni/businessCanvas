from django.contrib import admin

from .models import *
models = [
    KeyActivity, KeyPartner, KeyResource, ValueProposition,
    CustomerRelationship, CustomerSegment, Channel, CostStructure, RevenueStream
]
admin.site.register(models)
