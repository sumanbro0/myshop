from django import http
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Contact, OrderUpdate, Orders, product
from math import ceil
import json
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # products = product.objects.all()
    # n = len(products)

    allprods = []
    catprods = product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4+ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])
    params = {'allprods': allprods}
    return render(request, './shop/index.html', params)


def about(request):
    return render(request, './shop/about.html')


def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('ph.no', '')
        comment = request.POST.get('text', '')
        cont = Contact(name=name, email=email, phone=phone, comment=comment)
        cont.save()
        thank = True
    return render(request, './shop/contact.html', {'thank': thank, 'id': id})


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                        [updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, './shop/search.html')


def products(request, id):
    # fetch the product using id
    prods = product.objects.filter(id=id)

    return render(request, './shop/prodview.html', {'item': prods[0]})


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address2', '') + \
            " " + request.POST.get('address1', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email,
                       phone=phone, address=address, city=city, state=state, zip=zip,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The Order Has Been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, './shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, './shop/checkout.html')
