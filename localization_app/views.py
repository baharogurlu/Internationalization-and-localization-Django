from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.utils import translation

def index(request):
    """ Burası dil settings dosyasında ne olursa olsun burada belirtilen dili al demektir. ayrıca burası açılırsa
    urls.py dosyasında ki aşağıdaki alan kaldırılmalıdır.
        urlpatterns += i18n_patterns(
        path('localization_app/', include('localization_app.urls', namespace='localization_app')),
        prefix_default_language=False,
    )
    user_language='tr-tr'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY]=user_language
    """
    return render(request, 'localization_app/index.html')