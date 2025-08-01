from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('newsletter/', views.NewsletterView.as_view(), name='newsletter'),
    
    path('migrate/', views.MigrateView.as_view(), name='migrate'),    
    path("ping/", views.ping_view, name="ping"),
]
