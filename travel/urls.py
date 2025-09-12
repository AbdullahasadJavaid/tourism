
from django.urls import path
from .import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('place',views.place,name='place'),
    path('destination',views.destination,name='destination'),
    path('roombooking',views.roombooking,name='roombooking'),
    path('packagebooking',views.packagebooking,name='packagebooking'),
    path('contact',views.contact,name='contact'),
    path('currency',views.currency,name='currency'),
    path('login',views.login_user,name='login'),
    path('rooms',views.rooms,name='rooms'),
    path('registration',views.registration,name='registration'),
    path('logout',views.logout,name='logout'),
    path('confirm',views.confirm,name='confirm'),
    path('review', views.reviews,name="reviews"),
    path('hotel_register', views.hotel_register,name="register_hotel"),
    path('login_hotel', views.login_hotel,name="login_hotel"),
    path('hotel_site', views.hotel_site,name="hotel_site"),
    path('add_room', views.add_room,name="add_room"),
    path('add_package', views.add_package,name="add_package"),
    path('bookings',views.bookings,name="bookings"),
    path('userbookings',views.bookings_user,name="user_bookings"),
    path('test/',views.TestPage),
   
]
