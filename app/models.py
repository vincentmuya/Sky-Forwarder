from django.db import models

# Create your models here.
class NewForm(models.Model):
    SenderName=models.CharField(max_length = 2000)
    SenderAddress=models.CharField(max_length = 2000)
    RecieverName=models.CharField(max_length = 2000)
    RecieverAddress=models.CharField(max_length = 2000)
    referenceID=models.CharField(max_length = 2000)
    Origin=models.CharField(max_length = 2000,null=True)
    Destination=models.CharField(max_length = 2000,null=True)
    ScheduledFlight=models.CharField(max_length = 2000, null=True)
    DepatureDate=models.CharField(max_length = 2000)
    Depaturetime=models.CharField(max_length = 2000)
    ArrivalDate=models.CharField(max_length = 2000)
    ArrivalTime=models.CharField(max_length = 2000)
    Courier=models.CharField(max_length = 2000, null=True)
    InTransit=models.CharField(max_length = 2000, null=True)
    GoodsDescription=models.TextField(max_length = 5000)
    Status=models.TextField(max_length = 5000)


    def __str__(self):
        return self.referenceID

    @classmethod
    def search_by_referenceID(cls,search_term):
        results = cls.objects.filter(referenceID__icontains=search_term)
        return results

class Secure(models.Model):
    DepositorName=models.CharField(max_length = 2000)
    ReceiverName=models.CharField(max_length = 2000)
    TrackNo = models.CharField(max_length = 2000)
    Origin = models.CharField(max_length = 2000)
    Destination = models.CharField(max_length = 2000)
    ScheduledFlight=models.CharField(max_length = 2000, null=True)
    InTransit=models.CharField(max_length = 2000, null=True)
    TypeOfShipment = models.CharField(max_length = 2000)
    NatureOfGoods = models.TextField(max_length = 5000)
    Status = models.TextField(max_length = 5000)

    def __str__(self):
        return self.TrackNo

    @classmethod
    def search_by_TrackNo(cls,search_term):
        secure_result = cls.objects.filter(TrackNo__icontains=search_term)
        return secure_result
