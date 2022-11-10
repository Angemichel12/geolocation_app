from django.shortcuts import render, redirect
import requests
import json
from .models import Location,Contact
import folium
from folium import plugins
from .forms import PropertyRegister, RegistrationForm
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def home_page(request):
	return render(request, 'index.html')

@login_required
def map_page(request):
	data_list = Location.objects.values_list('latitude', 'longitude')
	map1 = folium.Map(location=[-1.952183, 30.054957], tiles='OpenStreetMap', zoom_start=9.5)
	plugins.FastMarkerCluster(data_list, icon=None).add_to(map1)

	map1 = map1._repr_html_()

	context = {
		'map1' : map1,
	}
	return render(request, 'map.html', context)

@login_required
def get_detail(request):
	if request.method == 'POST':
		ip = requests.get('https://api.ipify.org?format=json')
		ip_data = json.loads(ip.text)
		res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
		location_data_one = res.text
		location_data = json.loads(location_data_one)

		info = Location(poster=request.user,country=location_data['country'], latitude=location_data['lat'], longitude=location_data['lon'],
		city=location_data['city'], image=request.FILES.get('photo'), description=request.POST.get('message'),
		district=request.POST.get('district'), sector=request.POST.get('sector'), cell=request.POST.get('cell'),
		village=request.POST.get('village'))
		info.save()
		messages.success(request, f'Report is successfull!')
		return redirect('home')
	else:
	
		form=PropertyRegister()
	
	return render(request, 'report_form.html', context = {'form':form})

@login_required
def dashboard(request):
	datas = Location.objects.all()
	contacts=Contact.objects.all()
	
	data_list = Location.objects.values_list('latitude', 'longitude')
	map1 = folium.Map(location=[-1.952183, 30.054957], tiles='OpenStreetMap', zoom_start=9.5)
	plugins.FastMarkerCluster(data_list, icon=None).add_to(map1)

	map1 = map1._repr_html_()

	context = {
		'map1' : map1,
		'datas':datas,
		'contacts':contacts
	}
	return render(request, 'dashboard.html', context)


def registration(request):
    context = {}
    context['form'] = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('get_detail')
        else:
            context['form'] = form
    return render(request,'signup.html',context)


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("get_detail")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

@login_required
def detail(request, id):
	single_list = Location.objects.filter(pk=id).values_list('latitude', 'longitude')
	map1 = folium.Map(location=[-1.952183, 30.054957], tiles='OpenStreetMap', zoom_start=9.5)
	plugins.FastMarkerCluster(single_list, icon=None).add_to(map1)

	map1 = map1._repr_html_()

	obj = get_object_or_404(Location,pk=id)

	context = {
		'map1' : map1,
		'obj':obj,
	}
	return render(request, 'detail.html', context)

@login_required
def show(request):  
	contacts=Contact.objects.all()
	return render(request,"dashboard.html",{'contacts':contacts})


def contact(request):
	if request.method=="POST":
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		message=request.POST.get('message')

		en=Contact(name=name,email=email,subject=subject,message=message)
		en.save()
		
	return redirect('contact')

	
	
    # context = {}
    # context['form'] = ContactForm()

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if(form.is_valid()):
    #         form.save()
    #         return redirect('/')