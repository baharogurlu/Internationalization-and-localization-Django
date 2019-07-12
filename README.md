Aşağıdaki işlemlerin otomatik sağlanması için "GETTEXT" kütüphanesine ihtiyaç vardır!


1-) django-admin makemessages -l tr
 // tr .po dosyasının local adıdır.
 //Bu komut django projesinin root dizininde(manage.py içeren) ve uygulamaların root dizininde çalışır.
 // Sonucunda  locale/tr/LC_MESSAGES/django.po. gibi bir dizin açar


2-) makemessages -l de -e html
//django-admin makemessages default olarak .txt ve .html dosyalarını inceler
//Örneğin; eğer spesific olarak html sayfalarını incelemesini istiyorsak django-admin "makemessages -l de -e html" komutu ile sağlanır. "-e" option u ile sağlanır.
//Önemli!: eğer incelemesini dosyalarına bakmasını istiyorsak "djangojs" optionunu kullanmalıyız "-e" değil.


3-)django-admin makemessages -a
// yeni string ve template değişikleri durumunda güncelleme yapar.


4-)django-admin compilemessages
//Mesaj dosyaları oluşturulup güncellendikten sonra compile edilir.



GETTEXT#########################################

Download the following zip files from the GNOME servers(https://download.gnome.org/binaries/win32/dependencies/):
gettext-runtime-X.zip
gettext-tools-X.zip

Download the following zip files from the GNOME servers:
gettext-runtime-X.zip
gettext-tools-X.zip
(X is the version number; version 0.15 or higher is required.)

Extract the contents of the bin\ directories in both files to the same folder on your system (i.e. C:\Program Files\gettext-utils)
Update the system PATH:
Control Panel > System > Advanced > Environment Variables.
In the System variables list, click Path, click Edit.
Add ;C:\Program Files\gettext-utils\bin at the end of the Variable value field.
You may also use gettext binaries you have obtained elsewhere, so long as the xgettext --version command works properly. Do not attempt to use Django translation utilities with a gettext package if the command xgettext --version
entered at a Windows command prompt causes a popup window saying xgettext.exe has generated errors and will be closed by Windows.



###############################################################################
Projemizde translation işleminin aktiflşmesi için LANGUAGE_CODE(setting.py içerisinde) set edilmesi gerekir.
USE_I18N = True default olarak true oluşturulur.

// proje dizinine locale isimli dosya açılır!!
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)



MIDDLEWARE = [
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.locale.LocaleMiddleware',
   'django.middleware.common.CommonMiddleware',
]
'django.middleware.locale.LocaleMiddleware', kütüphanesi SessionMiddleware ve CommonMiddleware arasında olmalıdır.


LANGUAGES = (
    ('en-us', 'English'),
    ('tr-TR', 'Turkish'),
)





#############################################################
ERRORS
libstdc++-6.dll was not found error django makemessages
https://stackoverflow.com/questions/27220052/django-i18n-make-sure-you-have-gnu-gettext-tools

django-admin.py makemessages -l=ru -e=html,htm,txt---> libstdc++-6.dll hatası verirse libstdc++-6.dll kütüphanesini indir ve system32 directory altına koy ve restart yap




#############################################################
LİNKLER
https://samulinatri.com/blog/django-translation/

https://www.youtube.com/watch?v=xI97sLMd1rM

https://mlocati.github.io/articles/gettext-iconv-windows.html-->static olanın 64 bit olanı
