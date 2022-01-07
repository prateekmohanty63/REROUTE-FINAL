"""reroute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from fitness import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    #  path('',views.index,name='index'),
    # path('contact/',views.contact,name='contact'),
    # path('register/',views.register,name='register'),
    # path('login/',views.login,name='login'),
     path("payment/",views.payment,name="payment"),
    # path("about/",views.about,name="about"),
    # path("gallery/",views.gallery,name="gallery"),
    # path("event/",views.event,name="event"),
    path('',include('fitness.urls')),
    path("event_gallery/",views.event_img,name="event_gallery"),
    path("my_events/",views.my_event,name="my_event"),
    path('search_event/',views.search_event,name="search_event"),
    path('search_prog/',views.search_prog,name="search_prog"),
    path('event_reg/',views.event_reg,name="event_reg")
 
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
