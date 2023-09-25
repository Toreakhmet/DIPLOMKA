from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from mysite.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('cart',profile,name='profile'),
    path('books',book,name='book'),
    path('',include('django.contrib.auth.urls')),
    path('register/', register_view, name='register'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)