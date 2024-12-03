"""shopping URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path,include
from core import views as core
from item import views as item
from Message import views as Mes
from django.db.models import Q
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item.index, name='index-url'),
    path('contact/', core.contact, name='contact-url'),
    path('item/<int:id>/', item.detail, name='detail-url'),
    path('item/<int:id>/add_to_cart/', item.add_to_cart, name='add_to_cart'),
    path('cart/', item.view_cart, name='cart'),
    path('cart/<int:id>/remove/', item.remove_from_cart, name='remove_from_cart'),
    path('addnewitem/', item.new, name='new-url'),
    path('deleteitem/<int:id>/', item.delete, name='del-url'),
    path('edititem/<int:id>/', item.edit, name='edit-url'),
    path('search/', item.search, name='search-url'),
    path('signup/', core.signup, name='url_signup'),
    path('login/', core.login, name='url_login'),
    path('logout/', core.logout, name='url_logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('myitem/', item.show, name='show-url'),
    path('new_message/<int:item_id>/', Mes.NewMessage, name='new-message'),
    path('message_list/', Mes.message_list, name='message_list'),
    path('user_message/<int:user_id>', Mes.user_message, name='user_message'),
    url(r'^captcha',include('captcha.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

