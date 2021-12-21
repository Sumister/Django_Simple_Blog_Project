from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('search/', views.search, name='search'),
    path('signup/', views.handle_signup, name='handle_signup'),
    path('login/', views.handle_login, name='handle_login'),
    path('logout/', views.handle_logout, name='handle_logout'),

]
