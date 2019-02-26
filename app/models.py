from django.db import models

# Create your models here.
class NewForm(models.Model):
    SenderName=models.CharField(max_length = 2000)
    SenderAddress=models.CharField(max_length = 2000)
    RecieverName=models.CharField(max_length = 2000)
    RecieverAddress=models.CharField(max_length = 2000)
    referenceID=models.CharField(max_length = 2000)
    Origin=models.CharField(max_length = 2000)
    Destination=models.CharField(max_length = 2000)
    DepatureDate=models.DateTimeField(auto_now=False,blank=True)
    ArrivalDate=models.DateTimeField(auto_now = False,blank=True)
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
    TypeOfShipment = models.CharField(max_length = 2000)
    NatureOfGoods = models.TextField(max_length = 5000)
    Status = models.TextField(max_length = 5000)

    def __str__(self):
        return self.TrackNo

    @classmethod
    def search_by_TrackNo(cls,search_term):
        secure_result = cls.objects.filter(TrackNo__icontains=search_term)
        return secure_result
