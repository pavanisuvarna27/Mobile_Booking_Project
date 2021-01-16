from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Mobileapp.models import *
import datetime
# Create your models here.
class update(models.Model):
	g=[('Male','Male'),('Female','Female')]
	age=models.IntegerField(default=18)
	gender =models.CharField(choices=g,max_length=7)
	image=models.ImageField(upload_to="Profile_pics/",default='user.jpg')
	p=models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def creatprofile(sender,instance,created,**kwargs):
	if created:
		update.objects.create(p=instance)

class category(models.Model):
	name = models.CharField(max_length=20)

	@staticmethod
	def get_all_categories():
		return category.objects.all()

	def __str__(self):
		return self.name

class product(models.Model):
	name =models.CharField(max_length=50)
	price=models.IntegerField(default=0)
	category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
	description=models.TextField(max_length=200,default='')
	image=models.ImageField(upload_to="products/")

	@staticmethod
	def get_products_by_id(ids):
		return product.objects.filter(id__in =ids)

	@staticmethod
	def get_all_products():
		return product.objects.all()

	@staticmethod
	def get_all_products_by_categoryid(category_id):
		if category_id:
			return product.objects.filter(category = category_id)
		else:
			return product.get_all_products();

	def __str__(self):
		return self.name

class Order(models.Model):
    product = models.ForeignKey(product,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                                 on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_user(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')

    