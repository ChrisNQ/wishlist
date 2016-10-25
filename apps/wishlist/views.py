from django.shortcuts import render, redirect
from . models import Product, User
from django.contrib import messages
# from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    context = {
        'myproducts' : Product.objects.filter(users=User.objects.get(id=request.session['user']['id'])),
        'newproducts' : Product.objects.filter(wishlist_item=User.objects.filter(id=request.session['user']['id'])),
        "totalproducts" : Product.objects.exclude(users=User.objects.get(id=request.session['user']['id'])).exclude(wishlist_item=User.objects.filter(id=request.session['user']['id']))
    }
    return render(request, 'wishlist/index.html', context)

def addproduct(request):
    return render(request, "wishlist/add.html")

def add_wishlist(request): #creating
    result = Product.objects.validateproduct(request.POST, request.session['user']['id'])
    if result[0]:
        return redirect("wishlist:index")
    elif result[0] == False:
        errors = result[1]
        for error in errors:
            messages.error(request, error)
        return redirect("wishlist:addproduct")

def delete(request, id):
    Product.objects.get(id = id).delete()
    return redirect("wishlist:index")

def remove(request, id):
    Product.objects.delete(id, request.session['user']['id'])
    return redirect("wishlist:index")

def show(request, id):
    context = {
        "products": Product.objects.get(id=id)
    }
    return render(request, "wishlist/show.html", context)


def join(request, id):
    wishlist = Product.objects.get(id=id)
    user = User.objects.join(id, request.session['user']['id'])
    wishlist.ManyUsers.add(user)
    return redirect("wishlist:index")
