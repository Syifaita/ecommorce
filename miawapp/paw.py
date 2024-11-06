from djang.urls import path 
from miawapp.views import index
#from miawapp import *

app_name = "paw"

urlpatterns = [
    path("paw/", views.index)
]  