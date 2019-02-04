from django.db import models

# Create your models here.
class NewForm(models.Model):
    SenderName=models.CharField(max_length = 2000)
    SenderAddress=models.CharField(max_length = 2000)
    RecieverName=models.CharField(max_length = 2000)
    RecieverAddress=models.CharField(max_length = 2000)
    referenceID=models.CharField(max_length = 2000)
    GoodsareFrom=models.CharField(max_length = 2000)
    GoodsTo=models.CharField(max_length = 2000)
    DepatureDate=models.CharField(max_length = 2000)
    Depaturetime=models.CharField(max_length = 2000)
    ArrivalDate=models.CharField(max_length = 2000)
    ArrivalTime=models.CharField(max_length = 2000)
    GoodsDescription=models.TextField(max_length = 5000)
    Status=models.TextField(max_length = 5000)


    def __str__(self):
        return self.referenceID

    @classmethod
    def search_by_referenceID(cls,search_term):
        results = cls.objects.filter(referenceID__icontains=search_term)
        return results
