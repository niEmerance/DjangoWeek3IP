from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='projects'

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
    url(r'^new/project/', views.new_project, name = 'new-project'),
    url(r'profile/(\d+)', views.profile_view, name = 'profile'),
    url(r'update_profile/', views.update_profile, name = 'update_profile'),
    url(r'comment/(\d+)',views.comment_view,name="comment"),
    # url(r'^search/', views.searchProject, name='searchProject'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profile_api'),
    url(r'^api/project/$', views.ProjectList.as_view(),name='project_api')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)