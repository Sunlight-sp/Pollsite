from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('result/<int:pollId>',views.result,name='result'),
    path('vote/<int:pollId>',views.vote,name='vote'),

]