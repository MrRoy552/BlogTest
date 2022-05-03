from django.urls import path,include
from Blog.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router=DefaultRouter()
router.register('blog', blogView, basename='blog')
router.register('userRegisteration', userRegister, basename='userRegisteration')

urlpatterns = [
    
    path('',include(router.urls)),
    path('accounts/login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('accounts/refreshToken', jwt_views.TokenRefreshView.as_view(), name='RefreshToken'),
    # path('blog/blog', blogView.as_view(), name='blog'),
  
    
    
]