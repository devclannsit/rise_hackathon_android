from django.conf.urls import url
from users import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^makeaccount/$',views.makeaccount),
    url(r'^register/$',views.register,name='enter'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login1/$',views.login,name='login1'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^logout/$',views.logout,name='logout'),
        ]
