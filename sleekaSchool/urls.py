"""sleekaSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from courses import views as courses_views
# Not used: use the django-user-accounts library instead!
# from login import views as login_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', courses_views.home, name='home'),
    url(r'^enroll/$', courses_views.enroll, name='enroll'),
    url(r'^mySchedule/$', courses_views.mySchedule, name='mySchedule'),
    url(r'^clearSchedule/$', courses_views.clearSchedule, name='clearSchedule'),
    url(r'^optimizeSchedule/$', courses_views.optimizeSchedule, name='optimizeSchedule'),
    url(r'^registerAll/$', courses_views.registerAll, name='registerAll'),
    url(r"^account/", include("account.urls")),

    # NOT USED: use the django-user-accounts library instead!
    # login
    # url(r'^account/login/$', login_views.login, name='login'),
    # url(r'^accounts/auth/$', login_views.auth_view, name='auth'),
    # url(r'^accounts/logout/$', login_views.logout, name='settings'),
    # url(r'^accounts/loggedIn/$', login_views.loggedIn, name='loggedIn'),
    # url(r'^accounts/invalid/$', login_views.invalid, name='settings'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)