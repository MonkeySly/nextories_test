from django.urls import path
from calculator import views

app_name = "calculator"
urlpatterns = [
    path('index', view=views.index, name="index"),
    path('compute', view=views.compute, name="compute"),
    path('delete/<int:meuble_id>/', view=views.delete, name="delete"),
]
