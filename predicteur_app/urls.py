from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('activity/<int:activity_id>/', views.activity_detail, name='detail'),
    path('activities/', views.i_want_a_list, name='list_activities'),
    path('predict/', views.predict, name='to_predict')
]
