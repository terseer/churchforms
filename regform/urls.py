from django.conf.urls import url

from . import views

app_name = 'regform'

urlpatterns = [
    url(r'^section1$', views.section_1, name='section1'),
    url(r'^section2$', views.section_2, name='section2'),
    url(r'^section3$', views.section_3, name='section3'),
    url(r'^section4$', views.section_4, name='section4'),
    url(r'^registered$', views.registered)
]