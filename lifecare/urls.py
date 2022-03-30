from django.urls import path
app_name='lifecare'
from lifecare import views

urlpatterns = [
    path('',views.lifecare),

]