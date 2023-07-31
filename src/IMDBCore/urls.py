from django.conf.urls import url
# from django.conf import settings

# from .views import SubmitApi,SignupApi,LogoutApi,MediaApi,OrganisationList
from .views import (SubmitApi, 
                    SignupApi, 
                    LogoutApi)


app_name = "IMDBCore"

urlpatterns = [
    #url(r'^status/?$', StatusApi.as_view(), name='status'),
    url(r'^logout/?$', LogoutApi.as_view(), name='logout'),
    # url(r'^media/(?P<ftype>[^/]+)/(?P<filename>[^/]+)$',
        # MediaApi.as_view(), name='media'),
    url('SubmitApi', SubmitApi.as_view()),
    url('SignupApi', SignupApi.as_view()),
    # url('test_task', TestTaskApi.as_view()),
    # url('OrgList', OrganisationList.as_view())
]

