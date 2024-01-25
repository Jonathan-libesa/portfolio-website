from django.urls import path
from.import views

urlpatterns = [
    path('door-product',views.Door_product,name="product_door"),
    path('window-product',views.Window_product,name="product_window"),
    path('gate-product',views.Gate_product,name="product_gate"),

    path('quotation/<int:door_id>/', views.send_quotation, name='send_quotation'),

    path('quotation1/<int:window_id>/', views.send_quotation1, name='send_quotation1'),

    path('quotation2/<int:gate_id>/', views.send_quotation2, name='send_quotation2'),

] 