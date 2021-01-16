from django.shortcuts import render,redirect,HttpResponseRedirect
from Mobileapp.forms import UsersignupForm,updateform,imageprofile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Mobileapp.models import update
from django.core.mail import send_mail
from MobileStore import settings
from Mobileapp.models import *
from Mobileapp.models import product
# Create your views here.

def home(request):
	return render(request,'Mobileapp/home.html')

def about(request):
	return render(request,'Mobileapp/about.html')

def contact(request):
	return render(request,'Mobileapp/contact.html')

def authreg(request):
	if request.method == "POST":
		form=UsersignupForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			messages.warning(request,"Hi {} you are successfully registered".format(form.username))
			return redirect("/signin")
	form = UsersignupForm()
	return render(request,'Mobileapp/authreg.html',{'form':form})


@login_required
def dashboard(request):
	return render(request,'Mobileapp/dashboard.html')

@login_required
def profile(request):
	return render(request,'Mobileapp/profile.html')

@login_required
def update(request):
    if request.method == "POST":
        c = updateform(request.POST, instance=request.user)
        y = imageprofile(request.POST,request.FILES,instance=request.user.update)
        if c.is_valid() and y.is_valid():
            c.save()
            y.save()
            messages.success(request, "{} your details updated successfully".format(request.user.username))
            return redirect("/profile")
    c = updateform(instance=request.user)
    y = imageprofile(instance=request.user.update)
    return render(request, 'Mobileapp/update.html', {'b': c,'q':y})


@login_required
def mailsend(request):
	p=User.objects.values_list("email",flat=True)
	if request.method=='POST':
		#rc=request.POST['rcv'].split(",")
		z=[]
		a=request.user.email
		rs=list(filter(None,p))
		for n in rs:
			if n=='' or n==a:
				continue
			else:
				z.append(n)
		print(z)
		sb=request.POST['sub']
		mg=request.POST['msg']
		snd=settings.EMAIL_HOST_USER
		t=send_mail(sb,mg,snd,z)
		if t==1:
			messages.success(request,"mail send to {} successfully".format(z))
			return redirect('/Mobileapp/mailsend')
		messages.warning(request,"mail doesn't send because of invalid mailid {}".format(z))
	return render(request, 'Mobileapp/mailsend.html')

def Index(request):
    if request.method=='POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('home')



    if request.method=='GET':
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
	cart = request.session.get('cart')
	if not cart:
		request.session['cart'] = {}
	products = None
	categories = category.get_all_categories()
	categoryID = request.GET.get('category')

	if request.GET.get('id'):
		filterProductById = product.objects.get(id=int(request.GET.get('id')))
		return render(request, 'Mobileapp/productdetails.html',{"product":filterProductById,"categories":categories})

	if categoryID:
		products = product.get_all_products_by_categoryid(categoryID)
	else:
		products = product.get_all_products();

	data = {}
	data['products'] = products
	data['categories'] = categories
	print('you are : ', request.session.get('username'))
	return render(request,'Mobileapp/index.html',data)

def Cart(request):
    if request.method=='GET':
        ids = list(request.session.get('cart').keys())
        if request.GET.get('increase'):
            pId = request.GET.get('increase')
            products = request.session.get('cart')
            products[pId] += 1
            request.session['cart'] = products

        if request.GET.get('decrease'):
            pId = request.GET.get('decrease')
            products = request.session.get('cart')
            print(products[pId])
            if products[pId] > 1:
                products[pId] -= 1
                request.session['cart'] = products
                productList = list(request.session.get('cart').keys())
            else :
                del products[pId]
                request.session['cart'] = products
                productList = list(request.session.get('cart').keys())
        products = product.get_products_by_id(ids)
        print(products)
        return render(request , 'Mobileapp/cart.html' , {'products' : products} )

def CheckOut(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.session.get('User')
        cart = request.session.get('cart')
        products = product.get_products_by_id(list(cart.keys()))
        print(address, phone, user, cart, products)

        for productitem in products:
            print(cart.get(str(productitem.id)))
            order = Order(user=user,
                          product=productitem,
                          price=productitem.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(productitem.id)))
            order.save()
            sub  = 'Mobile Store Order'
            body = 'Hi '+request.user.username+'\n'+'Your order '+productitem.name+' successfully placed \n'+'Price: ₹'+str(productitem.price)+'\n'+'Quantity: '+str(order.quantity)
            receiver = request.user.email
            sender  = settings.EMAIL_HOST_USER
            send_mail(sub,body,sender,[receiver])
            messages.success(request,"Confirmation send to {} successfully ".format(receiver))
        request.session['cart'] = {}

        return redirect('cart')


def OrderView(request):
    if request.method=='GET':
        user = request.session.get('user')
        orders = Order.get_orders_by_user(user)
        print(orders)
        return render(request , 'Mobileapp/orders.html'  , {'orders' : orders})