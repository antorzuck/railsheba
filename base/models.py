from django.db import models


class Days(models.Model):
	day = models.CharField(max_length=20)
	
	def __str__(self):
		return self.day


class Station(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	

class Train(models.Model):
	train_name = models.CharField(max_length=20)
	start_point = models.CharField(max_length=50)
	end_point = models.CharField(max_length=50)
	time = models.TimeField()
	available_days = models.ManyToManyField(Days)
	station = models.ManyToManyField(Station)
	price = models.IntegerField(default=200)
	
	def __str__(self):
		return self.train_name


class Tariff(models.Model):
	starttoend = models.CharField(max_length=50)
	train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='tariffs')
	price = models.IntegerField()
	

class Seat(models.Model):
	train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='seats')
	seat = models.CharField(max_length=10)
	is_booked= models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.train)
		
		
class Ticket(models.Model):
	passanger = models.CharField(max_length=30)
	age = models.CharField(max_length=3)
	train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='tickets')
	price = models.CharField(max_length=40)
	seat = models.CharField(max_length=30)
