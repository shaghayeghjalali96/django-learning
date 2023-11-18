from django.urls import path
from basic_app import views


app_name = 'basic_app'
urlpatterns = [
    path("relative/", views.relative,name='relative'),
    path("others/",views.other,name='other'),
    path("other3",views.other),
]

# from django.conf.urls import url
# from basic_app import views

# # SET THE NAMESPACE!
# app_name = 'basic_app'

# urlpatterns=[
#     url(r'^relative/$',views.relative,name='relative'),
#     url(r'^other/$',views.other,name='other'),
# ]
