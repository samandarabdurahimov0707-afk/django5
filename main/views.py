from django.shortcuts import render
from .models import Car, Brand


def home(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()

    context = {
        'cars': cars,
        'brands': brands,
        'title': 'Mashinalar'
    }
    return render(request, 'main/index.html', context)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)

    context = {
        "car": car,
    }
    return render(request, 'main/detail.html', context)


def car_by_brand(request, brand_id):
    brands = Brand.objects.all()
    brand = Brand.objects.get(id=brand_id)
    cars = Car.objects.filter(brand_id=brand_id)

    context = {
        'brand': brand,
        'brands': brands,
        'cars': cars,
        'title': brand.name
    }
    return render(request, 'main/index.html', context)