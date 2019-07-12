"""localization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('localization_app/', include('localization_app.urls', namespace='localization_app')),
]
"""
urlpatterns += i18n_patterns(
    path('localization_app/', include('localization_app.urls', namespace='localization_app')),
    prefix_default_language=False,
    #http://127.0.0.1:8000/localization_app/ şeklinde default dili göstermesini istemiyorsak false, http://127.0.0.1:8000/en-us/localization_app/ göstermesini istiyorsak True yaparız
    #Bu kısım false olup setting.py de LANGUAGE_CODE ne belirtilirse onu yükler hiç belirtilmezse ingilizce yükler.
    #LANGUAGE_CODE belirtilmiş iken prefix_default_language=True olursa belirtilen dil ile linki getirir.
)"""