from django.db import models


class RouterDetails(models.Model):
    ROUTER_CHOICES = (
        ('AG', 'AG1'),
        ('CS', 'CSS'),
    )
    loopback = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    sap_id = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    router_type = models.CharField(max_length=5, choices=ROUTER_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{}".format(self.title)

    class Meta:
        unique_together = ("loopback", "hostname")


class Tenant(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Name: {} | Api Key: {}".format(self.name, self.token)
