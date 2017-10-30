from django.conf.urls import url
from . import views

#app_name = 'testbox'
urlpatterns = [
    url(r'showchat$', views.showchat, name='showchat'),
    #url(r'^getreply$',views.getreply),
    #url(r'^$', views.index, name='index'),

    #url(r'^signup$', views.signup, name='signup'),
    #/users/showdata:url to display the list of users stored on the database
   # url(r'^showdata$', views.showchat, name='showdata'),
]