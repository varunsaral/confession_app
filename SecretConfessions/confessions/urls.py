from django.urls import include, path
from . import views

urlpatterns = [
    path('secret_home/', views.home_secret, name='home'),
    path('', views.home, name='submit_confession'),
    path('thank-you/', views.thank_you, name='thank_you'),
    # path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs

]
