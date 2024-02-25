from django.db import models

# Create your models here.
class Continent(models.Model):
    name_continent= models.CharField(max_length=50)

class Pays(models.Model):
    name_pays= models.CharField(max_length=50)
    space= models.FloatField()
    population = models.IntegerField()
    device = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    Continent=models.ForeignKey(Continent,on_delete= models.DO_NOTHING, related_name='pays')



