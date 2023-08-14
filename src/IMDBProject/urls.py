"""IMDBProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# from django.http.multipartparser import MultiPartParser
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView
# from IMDBApp.views import (InsertMoviesData,
#                           GetDirectorWithMaxNumberOfMovies,
#                           GetTopTenMoviesBasedOnIMDBScore,
#                           GetLeastWatchedMovieBasedOnIMDBScore,
#                           GetMostWatchedGenre,
#                           GetMostPopularDirectorInFirstHundreadMovies,)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('insert/entire/data/', InsertMoviesData.as_view()),
#     path('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
#     path('get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view()),
#     path('get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
#     path('get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
#     path('get/most/watched/genre/', GetMostWatchedGenre.as_view()),
#     path('get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
# ]

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('insert/entire/data/', InsertMoviesData.as_view()),
    # path('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
    # path('get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view()),
    # path('get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
    # path('get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
    # path('get/most/watched/genre/', GetMostWatchedGenre.as_view()),
    # path('get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
    # path('openid/', include('djangooidc.urls')), 
    # path('api/IMDBApp/', include('IMDBApp.urls', namespace='IMDBApp'))

    # path(r'auth/', include('social_django.urls', namespace='social')), 
    path(r'api/IMDBApp/', include('IMDBApp.urls', namespace='IMDBApp'))

]
