from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import PPG
from .serializers import PpgSerializer
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # This is a view
    return HttpResponse("Your are on the main page: isn't it beautiful ?")

@csrf_exempt
def i_want_a_list(request):
    if request.method == "GET":
        activities = PPG.objects.all()
        serializer = PpgSerializer(activities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        content = JSONParser().parse(request)
        serializer = PpgSerializer(data = content)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def activity_detail(request, activity_id):
    try:
        activity = PPG.objects.get(pk=activity_id)
    except PPG.DoesNotExist:
        return HttpResponse(str(activity_id), status=404)
    if request.method == "GET":
        serializer = PpgSerializer(activity)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        # je recup le content du request et parse en JSON
        content = JSONParser().parse(request)
        # je serialise le JSON en instance de Activity
        serializer = PpgSerializer(activity) # , data = content)
 
        serializer.update(activity, content)

        return JsonResponse(serializer.data, status=201)
    elif request.method == "DELETE":
        activity.delete()
        return HttpResponse("Suppression faite!", status=204)

def predict_activity(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = ['WEIGHT',
 'Gender',
 'AGE',
 'HEIGHT',
 'SKIN',
 'SPORT',
 'Activity',
 'label',
 'ECG',
 'EMG',
 'EDA',
 'Temp',
 'Resp',
 'ACC1',
 'ACC2',
 'ACC3',
 'wACC1',
 'wACC2',
 'wACC3',
 'wBVP',
 'wEDA',
 'wTEMP']
    path_to_model   = "../models/randomforest.sav"
    path_for_scaler = "../models/sc.sav"
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    model           = joblib.load(path_to_model)
    scaler          = joblib.load(path_for_scaler)
    donnees_scalees = scaler.transform([unscaled_data])
    act            = model.predict(donnees_scalees)
    return act

@csrf_exempt
def predict(request):
    """
    Renvoie une activité
    
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = PpgSerializer(data=data)
        if serializer.is_valid():
            data["Activity"]        = predict_activity(data)
            serializer          = PpgSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)
