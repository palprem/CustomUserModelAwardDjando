from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # path('showdata/', views.showdata),
    path('register/', views.register),
    path('login/', views.login),
    path('award/', views.award),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)