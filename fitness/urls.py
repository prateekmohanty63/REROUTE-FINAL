from unicodedata import name
from django.urls import path
from. import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name="index"),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path("logout/",views.logout,name="logout"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("handlerequest/",views.handlerequest,name="HandleRequest"),
    path("payment",views.payment,name="payment"),
    path("about/",views.about,name="about"),
    path("gallery/",views.gallery,name="gallery"),
    path("event/",views.event,name="event"),                 # url for events
    path("event_gallery/",views.event_img,name="event_gallery"),   # url for event gallery
    path("my_events/",views.my_event,name="my_event"),            #  url for events attended by a user
    path('search_event/',views.search_event,name="search_event"),
    path('search_prog/',views.search_prog,name="search_prog"),
    path('event_reg/',views.event_reg,name="event_reg"),


    # dynamic urls
    path('event_reg/<pk>/',views.event_reg_try,name="event_reg_try"),
   

   # serializer paths
   path('get_event/<int:id>', Event_fetch.as_view()),
   path('get_event_list/',Event_list.as_view()),


   # Event registration
path('eventRegistration/<pk>/',views.eventRegistration,name="eventRegistration")

]