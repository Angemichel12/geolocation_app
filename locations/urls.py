from django.urls import path 
from .views import *
from geoLocations import settings
from django.conf.urls.static import static



urlpatterns = [
	path('', home_page, name='home'),
	path('map/', map_page, name='map'),
	path('get_detail/', get_detail, name='get_detail'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)