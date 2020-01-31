from django.db import models

# Create your models here.
class Activity(models.Model):
    WEIGHT      = models.FloatField()
    Gender      = models.BooleanField()
    AGE       	= models.FloatField()
    HEIGHT      = models.FloatField()
    SKIN        = models.FloatField()
    SPORT       = models.FloatField()
    Activity    = models.FloatField()
    label       = models.FloatField()
    ECG       	= models.FloatField()
    EMG         = models.FloatField()
    EDA     	= models.FloatField()
    Temp        = models.FloatField()
    Resp       	= models.FloatField()
	ACC1		= models.FloatField()
	ACC2		= models.FloatField()
	ACC3		= models.FloatField()
	wACC1		= models.FloatField()
	wACC2		= models.FloatField()
	wACC3		= models.FloatField()
	wBVP		= models.FloatField()
	wEDA		= models.FloatField()
	wTEMP		= models.FloatField()

    def __str__(self):
        return f'Une activité '
    # We don't have to...
    #class Meta:
    #    ordering = ['created']
