from django.conf.urls import url
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "libraryapp"

urlpatterns = [
    url(r'^$', book_list, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^book/form$', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    url(r'^librarians$', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    url(r'^libraries$', library_list, name='libraries'),
    path('library/<int:library_id>/', library_details, name='library'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^library/form$', library_form, name='library_form'),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
]