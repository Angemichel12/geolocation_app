from django.shortcuts import render, redirect
import requests
import json
from .models import Location
import folium
from folium import plugins

def home_page(request):
	return render(request, 'index.html')

def report(request):
	# Make request from ip-api.com
	ip = requests.get('https://api.ipify.org?format=json')
	ip_data = json.loads(ip.text)
	res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
	location_data_one = res.text
	location_data = json.loads(location_data_one)

	info = Location(country=location_data['country'], latitude=location_data['lat'], longitude=location_data['lon'])
	info.save()
	
	return redirect('home')

def map_page(request):
	data = Location.objects.all()
	data_list = Location.objects.values_list('latitude', 'longitude')
	map1 = folium.Map(location=[19, -12], tiles='CartoDB Dark_Matter', zoom_start=2)
	plugins.HeatMap(data_list).add_to(map1)

	map1 = map1._repr_html_()

	context = {
		'map1' : map1,
	}
	return render(request, 'map.html', context)

