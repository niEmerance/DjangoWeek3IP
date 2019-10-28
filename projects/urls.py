from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static

app_name='projects'

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
]