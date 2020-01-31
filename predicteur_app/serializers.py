from rest_framework import serializers
from predicteur_app.models import PPG


class PPGSerializer(serializers.Serializer)  :
    """ to serialize or deserialize data
    -> Serialize                               : model instance / querysets => native Python datatypes => JSON
        ** NETWORK **
    -> Deserialize                             : JSON to model instance
    """

    WEIGHT      = serializers.FloatField()
    Gender      = serializers.BooleanField()
    AGE         = serializers.FloatField()
    HEIGHT      = serializers.FloatField()
    SKIN        = serializers.FloatField()
    SPORT       = serializers.FloatField()
    label       = serializers.FloatField()
    ECG         = serializers.FloatField()
    EMG         = serializers.FloatField()
    EDA         = serializers.FloatField()
	Temp        = serializers.FloatField()
    Resp        = serializers.FloatField()
    ACC1        = serializers.FloatField()
	ACC2        = serializers.FloatField()
    ACC3        = serializers.FloatField()
    wACC1       = serializers.FloatField()
	wACC2       = serializers.FloatField()
    wACC3       = serializers.FloatField()
    wBVP        = serializers.FloatField()
	wEDA        = serializers.FloatField()
    wTEMP       = serializers.FloatField()
	
	Activity    = serializers.FloatField(allow_null=True)
  

    def create(self, validated_data)           :
        """ Create and return a new Activity instance, given the validated data """
        return PPG.objects.create(**validated_data)

    def update(self, instance, validated_data) :
        """ Update and return an existing 'Activity' instance, given the validated data """
        instance.WEIGHT    = validated_data.get('WEIGHT' , instance.WEIGHT)
        instance.Gender      = validated_data.get('Gender' , instance.Gender)
        instance.AGE    = validated_data.get('AGE' , instance.AGE)
        instance.HEIGHT     = validated_data.get('HEIGHT' , instance.HEIGHT)
        instance.SKIN      = validated_data.get('SKIN' , instance.SKIN)
        instance.SPORT     = validated_data.get('SPORT' , instance.SPORT)
        instance.label     = validated_data.get('label' , instance.label)
        instance.ECG = validated_data.get('ECG' , instance.ECG)
        instance.EMG   = validated_data.get('EMG' , instance.EMG)
        instance.EDA   = validated_data.get('EDA' , instance.EDA)
		instance.Temp   = validated_data.get('Temp', instance.Temp)
		instance.Resp   = validated_data.get('Resp' , instance.Resp)
		instance.ACC1   = validated_data.get('ACC1' , instance.ACC1)
		instance.ACC2   = validated_data.get('ACC2' , instance.ACC2)
		instance.ACC3   = validated_data.get('ACC3' , instance.ACC3)
		instance.wACC1   = validated_data.get('wACC1' , instance.wACC1)
		instance.wACC2   = validated_data.get('wACC2' , instance.wACC2)
		instance.wACC3   = validated_data.get('wACC3' , instance.wACC3)
		instance.wBVP   = validated_data.get('wBVP' , instance.wBVP)
		instance.wEDA   = validated_data.get('wEDA' , instance.wEDA)
		instance.wTEMP   = validated_data.get('wTEMP' , instance.wTEMP)
		
		#instance.Activity     = validated_data.get('Activity' , instance.Activity)
		
		
        instance.save()
        return instance
