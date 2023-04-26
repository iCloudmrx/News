from django.urls import path
from .views import (post_404, post_contact,
                    post_detail, post_index, localView,
                    admin_page, ContactView, searchposts,
                    aboutListView, xorijView, sportView,
                    texView, SearchResultsView, post_share
                    )

app_name = 'blog'
urlpatterns = [
    path('', post_index, name='post_index'),
    path('contact/', post_contact, name='contact'),
    path('404/', ContactView.as_view(), name='404'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail,
         name='post_detail'),
    path('Mahalliy/', localView, name='local'),
    path('adminpage/', admin_page, name='admin_page'),
    path('about/', aboutListView, name='about'),
    path('Xorij/', xorijView, name='xorij'),
    path('Sport/', sportView, name='sport'),
    path('Texnologiya/', texView, name='texno'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:post_id>/share/', post_share, name='share')
]
