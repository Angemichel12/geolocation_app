from django.shortcuts import render, redirect
import requests
import json
from .models import Location
import folium
from folium import plugins
from .forms import PropertyRegister
from django.contrib import messages

def home_page(request):
	return render(request, 'index.html')


def map_page(request):
	data = Location.objects.all()
	data_list = Location.objects.values_list('latitude', 'longitude')
	map1 = folium.Map(location=[-1.952183, 30.054957], tiles='OpenStreetMap', zoom_start=9.5)
	plugins.FastMarkerCluster(data_list, icon=None).add_to(map1)

	map1 = map1._repr_html_()

	context = {
		'map1' : map1,
	}
	return render(request, 'map.html', context)

def get_detail(request):
	if request.method == 'POST':
		ip = requests.get('https://api.ipify.org?format=json')
		ip_data = json.loads(ip.text)
		res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
		location_data_one = res.text
		location_data = json.loads(location_data_one)

		info = Location(country=location_data['country'], latitude=location_data['lat'], longitude=location_data['lon'],
		city=location_data['city'], street=location_data['regionName'], image=request.FILES.get('photo'), description=request.POST.get('message'))
		info.save()
		messages.success(request, f'Report is successfull!')
		return redirect('home')
	else:
	
		form=PropertyRegister()
	
	return render(request, 'report_form.html', context = {'form':form,})