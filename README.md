
## Projenin yapılış aşamaları

sudo apt-get install python3-virtualenv



1) home da  

#virtualenv velespi
#cd velespi
#source bin/activate


2) virt.env aktifken home da

#pip install Pillow
****** hata verirse:    #sudo apt-get install libjpeg-dev
#mkdir lyk-project
#cd lky-project
#django-admin startproject velespi
#cd velespi
#pip install Django
#python manage.py runserver


*****  Dili Türkçe yapmak için settings.py da 106.satır
    LANGUAGE_CODE = 'tr-TR'


3) velespi nin içinde yeni bir app oluşturduk
#python manage.py startapp places

4) Oluşturduğumuz app i projeye dahil etmek için 
settings.py de   'places'  ekledik


5) model.py da database tabanlı classlar oluşturduk

-class Place
-class Category
-class Review
-class Media

*****  null=True :validation boşluğuna bakar
         blank=True :  veri tabanı boşluğuna bakar 


6) Database i güncellemek için ; model oluşturduktan sonra 

#python manage.py makemigrations
#python manage.py migrate


7) Bir admin oluşturduk

#python manage.py createsuperuser

***** Daha basit bir admin şifresi oluşturabilmek için
setting.py da

if not DEBUG:

    AUTH_PASSWORD_VALIDATORS = [


8) Kullanıcının görebileceği kısmı düzenlemek için :

admin.py 

***** class MediaInline(admin.StackedInline):
      class MediaInline(admin.Inline):

9) templates klasörü oluşturduk 


***** settings.py da
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],


10) HTML dosyaları oluşturduk

base.html
index.html
place.html 


11) urls.py da sayfaların url lerini belirttik.



***** html de veri çekerken

-{{ place.name }} : place in name ini çeker

-{{ place.description | linebreaksbr}}  : place in desc. ını çeker 

-{% for review in place.review_set.all %} : o place e bağlı review ları çeker.
 

12) model.py da PlaceManager classını oluşturduk

Filtrelemeleri tek bir yerde tutmak, tekrar tekrar kulanabilmek için

girilen yerler database de olduğu halde, eğğer kullanıcı aktif değilse hem admin panelinde hemde arayüzde o kullanıcıya ait yazılar gözükmesin.

***** user__is_active : __ nokta yerine kullanılıyor. python ın özelliği.


13) python manage.py startapp profiles

yeni sayfalar ekledik
view.py da sayfaları açtık
templates in içine bunların html lerini açtık

register.html
login.html
logout.html

14) registration formu için  forms.py oluşturduk

hazır formlar kullandık, formda gelmeyenleri meta class ının içinde oluşturduk


15) python3 manage.py runserver da sessin hatası çözümü

settings.py    MIDDLEWARE_CLASSES


16) js le harita ekledik.

base.html ve index.html de
istediğimiz yerin koordinatlarını ekliyoruz


17) haritadan tıklayarak koordinat eklemek için new_place.html oluşturduk ve marker ları belirledik.

18) html den fotoğraf ekleme sayfası yaptık
new_media.html 

