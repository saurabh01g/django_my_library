"""my_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document

from book import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
print("In urls.py")

"""
django-debug-toolbar is used.
<int:id> --- regular expression : <id>[0-9]+ means any combination of 0to9 digits. i.e. integer value
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name="homepage"),
    path('show-all-active-books/', views.show_all_active_books, name="show_all_active_books"),
    path('show-all-inactive-books/', views.show_all_inactive_books, name="show_all_inactive_books"),
    path('edit/<int:id>/', views.edit_data, name="edit"),                                                    #<id>[0-9]+ : regular expression
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('delete-all-data/', views.delete_all_data, name="delete_all_data"),
    path('soft-delete/<int:id>/', views.soft_delete_data, name="soft_delete"),
    path('soft-delete-all-data/', views.soft_delete_all_data, name="soft_delete_all_data"),
    path('restore/<int:id>/', views.restore_data, name="restore"),
    path('__debug__/', include('debug_toolbar.urls')),
    path('',views.welcome, name="welcome "),
    path('feedback-form', views.Feedback_Form, name="feedback_form"),
    path('book-model-form', views.Book_Model_Form, name="book_model_form"),
    path('address-form', views.Address_Form, name="address_form"),
    path('contact-form', views.Contact_Form, name="contact_form"),

    path('home_cbv/', views.HomePage.as_view(), name="homepage1"),


    path('', include(('book.urls'), namespace='book')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]