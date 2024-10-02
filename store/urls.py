from django.urls import path
from . import views

urlpatterns = [
    path('', views.weapon_list, name='weapon_list'),  # قائمة الأسلحة
    path('accessories/', views.accessory_list, name='accessory_list'),  # قائمة الإكسسوارات
    path('weapons/<int:id>/', views.weapon_detail, name='weapon_detail'),  # تفاصيل السلاح
    path('accessories/<int:id>/', views.accessory_detail, name='accessory_detail'),  # تفاصيل الإكسسوار
]

