# """IMDBProject URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView
# from IMDBApp.views import (InsertMoviesData,
#                           GetDirectorWithMaxNumberOfMovies,
#                           GetTopTenMoviesBasedOnIMDBScore,
#                           GetLeastWatchedMovieBasedOnIMDBScore,
#                           GetMostWatchedGenre,
#                           GetMostPopularDirectorInFirstHundreadMovies,)

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('insert/entire/data/', InsertMoviesData.as_view()),
# #     path('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
# #     path('get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view()),
# #     path('get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
# #     path('get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
# #     path('get/most/watched/genre/', GetMostWatchedGenre.as_view()),
# #     path('get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
# # ] + \
# # []
# # [path(r'/keycloak/')]


# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('accounts/insert/entire/data/', InsertMoviesData.as_view()),
# #     path('accounts/get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
# #     path('accounts/get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view()),
# #     path('accounts/get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
# #     path('accounts/get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
# #     path('accounts/get/most/watched/genre/', GetMostWatchedGenre.as_view()),
# #     path('accounts/get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
# # ] + \
# # [path('accounts/', include('django.contrib.auth.urls'))]


# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('insert/entire/data/', InsertMoviesData.as_view()),
# #     path('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
# #     path('get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view()),
# #     path('get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
# #     path('get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
# #     path('get/most/watched/genre/', GetMostWatchedGenre.as_view()),
# #     path('get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
# # ] + \
# # []
# # # [path(r'openid/', include('djangooidc.urls')), 
# # #  ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('insert/entire/data/', InsertMoviesData.as_view()),
#     path('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
#     path('get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view(), name='top_director'),
#     path('get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
#     path('get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
#     path('get/most/watched/genre/', GetMostWatchedGenre.as_view()),
#     path('get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
#     # path('http://127.0.0.1:8080/realms/myrealm/protocol/openid-connect/auth?client_id=manvesh&response_type=code&redirect_uri=http://127.0.0.1:8000/', )
# ] + \
# []
# # [path(r'openid/', include('djangooidc.urls')), 
# #  ]


from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from IMDBCore.views import main_view, login_view, logout_view

admin.autodiscover()
admin.site.site_header = 'IMDB Administration'
admin.site.site_title = 'IMDB Administration'
admin.site.index_title = 'IMDB Objects'

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path(r'auth/', include('social_django.urls', namespace='social')),
    path(r'sentry-debug/', trigger_error),
    path(r'logout', logout_view),
    path(r'login', login_view),
    # path(r'^keycloak/', include('django_keycloak.urls',namespace='keycloak')),
    path(r'api/IMDBCore',include('IMDBCore.urls',namespace='IMDBCore')),
    path(r'api/IMDBApp',include('IMDBApp.urls',namespace='IMDBApp')),
    # path(r'api/django_trainer_roi',include('django_trainer_roi.urls',namespace='django_trainer_roi')),
    # path(r'api/regex_core',include('regex_core.urls',namespace='regex_core')),
    re_path(r'.*', main_view),
    # path('manage/', admin.site.urls),
]