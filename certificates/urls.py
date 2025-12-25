
from django.urls import path
from .views import certificate_list, certificate_create, certificate_verify, home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('certificates/list/', certificate_list, name='certificate_list'),
    path('create/', certificate_create, name='certificate_create'),
    path('certificates/verify/<str:certificate_id>/', certificate_verify, name='certificate_verify'),
]
