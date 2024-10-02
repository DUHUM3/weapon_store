from django.shortcuts import render, get_object_or_404
from .models import Weapon,Accessory

def weapon_list(request):
    weapons = Weapon.objects.all()
    return render(request, 'store/weapon_list.html', {'weapons': weapons})

def weapon_detail(request, id):
    weapon = get_object_or_404(Weapon, id=id)
    return render(request, 'store/weapon_detail.html', {'weapon': weapon})

def accessory_list(request):
    accessories = Accessory.objects.all()
    return render(request, 'store/accessory_list.html', {'accessories': accessories})

def accessory_detail(request, id):
    accessory = get_object_or_404(Accessory, id=id)
    return render(request, 'store/accessory_detail.html', {'accessory': accessory})