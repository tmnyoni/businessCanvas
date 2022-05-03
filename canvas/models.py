from django.db import models


class KeyPartner(models.Model):
    class Meta:
        db_table = "KeyPartners"

    partner = models.CharField(max_length=50)


class KeyActivity(models.Model):
    class Meta:
        db_table = "KeyActivities"

    activity = models.CharField(max_length=100)


class KeyResource(models.Model):
    class Meta:
        db_table = "KeyResources"

    resource = models.CharField(max_length=200)


class ValueProposition(models.Model):
    class Meta:
        db_table = "ValuePropositions"

    proposition = models.CharField(max_length=100)


class CostStructure(models.Model):
    class Meta:
        db_table = "CostStructure"

    structure = models.CharField(max_length=100)


class CustomerRelationship(models.Model):
    class Meta:
        db_table = "CustomerRelationships"

    relationship = models.CharField(max_length=200)


class Channel(models.Model):
    class Meta:
        db_table = "Channels"

    channel = models.CharField(max_length=100)


class CustomerSegment(models.Model):
    class Meta:
        db_table = "CustomerSegments"

    segment = models.CharField(max_length=200)


class RevenueStream(models.Model):
    class Meta:
        db_table = "RevenueStreams"

    stream = models.CharField(max_length=100)
