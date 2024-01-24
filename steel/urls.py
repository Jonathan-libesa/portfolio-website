from django.urls import path
from.import views

urlpatterns = [
    path('',views.homeview,name="home"),
    path('contact_ndonga_and_son enterprise',views.contact,name="contact_open"),
    #path('about ',views.aboutpage,name="about"),
 ] 