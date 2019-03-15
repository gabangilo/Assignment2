# used to get other urls from other .py files in project
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # map to separate admin url
    path('register/', user_views.register, name = 'register'),  # map to register url
    path('profile/', user_views.profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),  # map to login url
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),  # map to logout url
    path('', include('blog.urls')),  # used to map to blog apps urls
]
#  this allows media files to work in browsers
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)