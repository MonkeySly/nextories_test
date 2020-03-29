from django.urls import path
from calculator import views

app_name = "calculator"
urlpatterns = [
    path('index', view=views.index, name="index"),
]
