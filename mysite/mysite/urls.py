"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from pages.views import login_view, register_view, logout_pag
from products.views import product_view, busca_view
from buy.views import cart_view, cart_delete, add_item_cart

urlpatterns = [
    path('', product_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_pag, name='log_out'),
    path('register/', register_view, name='register'),

    path('busca/', busca_view, name='busca'),

    path('cart/', cart_view, name='cart'),
    path('delete/<item_id>', cart_delete, name='cart_delete'),
    path('add/<item>', add_item_cart, name='cart_add'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)