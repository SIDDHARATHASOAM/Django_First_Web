from django.contrib import admin
from django.urls import path, include
from car_wash_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="home"),
    path('about/', views.about , name="about"),
    path('contact/', views.contact , name="contact"),
    path('services/', views.services , name="services"),
    path('blogs/', views.blogs , name="blogs"),
    path('login/', views.login , name="login")
    

] 