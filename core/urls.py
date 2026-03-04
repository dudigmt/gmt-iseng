from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('hr/', views.hr_dashboard, name='hr_dashboard'),
    path('production/', views.production_dashboard, name='production_dashboard'),
    path('finance/', views.finance_dashboard, name='finance_dashboard'),
    path('sales/', views.sales_dashboard, name='sales_dashboard'),

]

