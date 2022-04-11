import datetime
import os
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from base.models import *


# Create your views here.
def home(request):
	return render(request, 'home.html')
	
	
def search(request):
	fm = request.GET['from']
	to = request.GET['to']
	date = request.GET['date'].split("-")
	list = []
	for i in date:
		list.append(int(i))
		
	day = datetime.datetime(list[0],list[1],list[2]).strftime("%A")
	
	days = Days.objects.get(day=day)
	trains = Train.objects.filter(Q(start_point=fm, end_point=to) & Q(available_days=days))
	
	context = {"trains":trains}
	return render(request, 'search.html', context)
	

def get_ticket(request, id):
	train = Train.objects.get(id=id)
	left_seat = train.seats.all()[0:10]
	right_seat = train.seats.all()[10:20]
	tariff = train.tariffs.all()
	sep = request.GET.get('sp')
	context = {"price" : train.price, 'tariff':tariff, 'ls':left_seat, 'rs':right_seat, 'train':train}
	if sep:
		t = Tariff.objects.get(id=sep)
		price = t.price
		context['price'] = price
	return render(request, 'ticket.html', context)
	

def create_ticket(request):
	sits = request.POST['seats']
	name = request.POST['pn']
	age = request.POST['pa']
	price = request.POST['pric']
	train_id = request.POST['tran']
	train = Train.objects.get(id=train_id)
	
	ticket = Ticket.objects.create(passanger=name, age=age, price=price,train=train, seat=sits)
	
	booked = Seat.objects.get(id=sits)
	booked.is_booked = True
	booked.save()
	context = { 'ticket' : ticket }
	return render(request, 'success.html', context)
	

def download_ticket(request):
	from reportlab.pdfgen import canvas
	
	if request.method == 'POST':
		id = request.POST.get('id')
		t = Ticket.objects.get(id=id)
		l = [t.passanger, t.train, t.price, t.seat]
		name = str(random.randint(1111,9999)) + '.pdf'
		
		path = '/media'
		o_path = os.path.join(path, name)
		pdf = canvas.Canvas(o_path)
		for i in l:
			pdf.drawLines(l)
		pdf.save()
		
		return redirect(f'/media/{name}')
	
