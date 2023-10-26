#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'restaurant'

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(),name="menu-view"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('', views.index, name='index'),

]
