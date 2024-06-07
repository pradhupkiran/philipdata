from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)
    website=models.CharField(max_length=250,blank=True,null=True)
    email_id=models.EmailField(max_length=250,blank=True,null=True)
    email_id_2=models.EmailField(max_length=250,blank=True,null=True)
    tel_no=models.CharField(max_length=15,blank=True,null=True)
    address=models.TextField(max_length=250,blank=True,null=True)
    address2=models.TextField(max_length=250,blank=True,null=True)
    city=models.CharField(max_length=25,blank=True,null=True)
    town=models.CharField(max_length=25,blank=True,null=True)
    country=models.CharField(max_length=75,blank=True,null=True)
    technology=models.CharField(max_length=250,blank=True,null=True)
    technology_2=models.CharField(max_length=250,blank=True,null=True)
    technology_3=models.CharField(max_length=250,blank=True,null=True)
    contact_person=models.CharField(max_length=250,blank=True,null=True)

    class Meta:
        ordering=('name',)
        verbose_name='detail'
        verbose_name_plural='details'

    def __str__(self):
        return '{}'.format(self.name)