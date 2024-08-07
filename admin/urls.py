from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',views.admin_dashboard),
    path('profile/',views.profile),
    path('profile/save/',views.save),
    path('logout/',views.logout),
    path('manage_places/',views.manage_places),
    path('admin_create/',views.manage_admin),
    path('driver/create/',views.manage_driver),
    path('driver/details/',views.driver_details),
    path('requests/details/',views.request_details),
]