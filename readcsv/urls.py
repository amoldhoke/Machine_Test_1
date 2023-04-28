from django.urls import path
from readcsv import views

urlpatterns = [
    path('', views.home, name='home'),
    # Path to delete the message
    path('delete_message/<str:customer_id>', views.delete_message, name="delete_message"),
]