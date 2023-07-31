from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls import url
from IMDBApp.views import (InsertMoviesData,
                          GetDirectorWithMaxNumberOfMovies,
                          GetTopTenMoviesBasedOnIMDBScore,
                          GetLeastWatchedMovieBasedOnIMDBScore,
                          GetMostWatchedGenre,
                          GetMostPopularDirectorInFirstHundreadMovies,)


app_name = 'IMDBApp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('insert/entire/data/', InsertMoviesData.as_view()),
    url('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
    url('get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view(), name='top_director'),
    url('get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
    url('get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
    url('get/most/watched/genre/', GetMostWatchedGenre.as_view()),
    url('get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
    # path('http://127.0.0.1:8080/realms/myrealm/protocol/openid-connect/auth?client_id=manvesh&response_type=code&redirect_uri=http://127.0.0.1:8000/', )
] + \
[]
