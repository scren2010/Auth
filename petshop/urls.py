from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/login/', include('rest_auth.registration.urls')),

    path('accounts/', include('allauth.urls')),
    path('accounts/logout/', include('allauth.urls')),
    path('accounts/google/login/', include('allauth.urls')),

    path('api/v1/', include('backend.user_profile.urls')),
]
