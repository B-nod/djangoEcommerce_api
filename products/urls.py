from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('product/',  views.ProductList.as_view(),name="product"),
    # path('product/<int:pk>/', views.ProductUpdate.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryUpdate.as_view()),
    path('order/', views.OrderList.as_view(),name="order"),
    path('order/<int:pk>/', views.OrderUpdate.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserUpdate.as_view()),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('product/',  views.product_list,name="product"),
    path('product/<int:pk>/', views.product_detail),
]