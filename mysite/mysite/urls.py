from django.contrib import admin
from django.urls import path
from myapp.views import blogs, about, blog_post, cip, ufp, dp, change_password, login, profile, register, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogs, name='blogs'),
    path('blogs/', blogs, name='blogs'),
    path('about/', about, name='about'),
    path('', blogs, name='blogs'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('register/', register, name='register'),
    path('<slug:name>/', blog_post, name='blog_post'),
    path('<slug:name>/comment/', cip, name='comment_in_post'),
    path('<slug:name>/update/', ufp, name='update_for_post'),
    path('<slug:name>/delete/', dp, name='delete_post'),
]
