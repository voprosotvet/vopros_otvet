from django.urls import path
from .views import *

urlpatterns = [
    path('', NewListView.as_view(), name='index'),


    path('search/', SearchNew.as_view(), name='search'),
    path('about_page/', about_page, name='about_page')

]