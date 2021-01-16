from django.urls import path
from Mobileapp import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	path('',views.Index,name='home'),
	path('store', views.store, name='store'),
	path('about/',views.about,name="about"),
	path('contact/',views.contact,name="contact"),
	path('signup/',views.authreg,name="signup"),
	path('dashboard/',views.dashboard,name='dashboard'),
	path('profile/',views.profile,name='profile'),
	path('update/',views.update,name='update'),
	path('mailsend',views.mailsend,name="mailsend"),
	path('signin/',auth_views.LoginView.as_view(template_name='Mobileapp/signin.html'),name='signin'),
	path('signout/',auth_views.LogoutView.as_view(template_name='Mobileapp/logout.html'),name='signout'),
	path('cart/', views.Cart, name='cart'),
	path('check-out', views.CheckOut , name='checkout'),
	path('orders/',views.OrderView, name='orders'),
]