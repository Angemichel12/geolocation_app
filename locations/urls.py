from django.urls import path 
from .views import *
from .apiviews import LocationList, LocationDetail
from geoLocations import settings
from django.conf.urls.static import static



urlpatterns = [
	path('', home_page, name='home'),
	path('map/', map_page, name='map'),
	path('get_detail/', get_detail, name='get_detail'),
	path('dashboard/', dashboard, name='dashboard'),
	path('sign-up/',registration,name='signup'),
    path("login/", login_request, name="login"),
    path("detail/<int:id>", detail, name="datail"),
	path('contact/',contact,name='contact'),
	path('show/',show,name='show'),
    path('locations/', LocationList.as_view(), name='locatons_list'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location_detail'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)