from django.urls import path 
from .views import *



urlpatterns = [
	path('', home_page, name='home'),
	path('map/', map_page, name='map'),
	path('report/', report, name='report'),

]