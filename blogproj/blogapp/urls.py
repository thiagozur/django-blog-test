from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('makepost/', views.posting, name='posting'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('auth/', views.auth, name='auth'),
    path('newuser/', views.newuser, name='newuser'),
    path('delpost/<postslug>', views.delpost, name='delpost'),
    path('togglepost/<postslug>', views.togglepost, name='togglepost'),
    path('repub/<postslug>', views.repub, name='repub'),
    path('postedit/<postslug>', views.postedit, name='postedit'),
    path('<slug:post>/', views.post_single, name='post_single'),
]