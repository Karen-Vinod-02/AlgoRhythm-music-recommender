from django.urls import path
from . import views  
from .views import register, login_view, logout_view, home_view, recommend_view
from django.templatetags.static import static 
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.register, name='register'),  # We're using registration as the default page
    path('login/', views.login_view, name='login'),  
    path('logout/', logout_view, name="logout"), 
    path('home/', views.home_view, name='home'), 
    path('recommend/', views.recommend_view, name='recommend'),  # Seperate page for displaying the recommendations 
    path('favicon.ico', RedirectView.as_view(url=static('musicrec_app/images/favicon.ico'), permanent=True)), #To remove the favicon errors
]
