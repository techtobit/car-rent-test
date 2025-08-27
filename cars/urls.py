from django.urls import path
from . import views

urlpatterns = [
    path('add_cars/', views.AddCar.as_view(), name='add_cars'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
    path('buy_car/<int:id>/', views.buy_car , name='buy_car'),
    # path('profile/', views.ProfileView.as_view() , name='profile')
    # path('profile/', views.ProfileViews , name='profile')
    path('profile/', views.ProfileView , name='profile')
]
