from django.urls import path, include
from admin_app import views

#TEMPLATE URLS!!!!!
app_name = "admin_app"

urlpatterns = [
    path('register/',views.register,name="register"),
    path('farmer/',views.farmer,name="farmer"),
]
