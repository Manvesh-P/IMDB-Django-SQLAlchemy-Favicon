from django.contrib import admin
# from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from IMDBApp.views import (
                        #   GetToken, 
                          HomeView, 
                          LogOut, 
                          InsertMoviesData,
                          GetDirectorWithMaxNumberOfMovies,
                          GetTopTenMoviesBasedOnIMDBScore,
                          GetLeastWatchedMovieBasedOnIMDBScore,
                          GetMostWatchedGenre,
                          GetMostPopularDirectorInFirstHundreadMovies,)
from django.conf.urls import url


app_name = 'IMDBApp'

# urlpatterns = [
#     url('admin/', admin.site.urls),
#     # url('get_token/', GetToken.as_view()), 
#     # url('home/view/', HomeView.as_view()),
#     # url('/', HomeView.as_view()), 
#     url('logout/', LogOut.as_view()), 
#     url('insert/entire/data/', InsertMoviesData.as_view()),
#     url('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
#     url('get/director/with/max/number/of/movies/', GetDirectorWithMaxNumberOfMovies.as_view()),
#     url('get/top/ten/movies/based/on/imdb_score/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
#     url('get/least/watched/movie/based/on/imdb_score/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
#     url('get/most/watched/genre/', GetMostWatchedGenre.as_view()),
#     url('get/most/popular/director/in/first/hundread/movies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
# ]


urlpatterns = [
    url('admin/', admin.site.urls),
    # url('get_token/', GetToken.as_view()), 
    url('home/view/', HomeView.as_view()),
    # url('/', HomeView.as_view()), 
    url('logout/', LogOut.as_view()), 
    url('insert/entire/data/', InsertMoviesData.as_view()),
    url('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
    url('GetDirectorWithMaxNumberOfMovies/', GetDirectorWithMaxNumberOfMovies.as_view()),
    url('GetTopTenMoviesBasedOnIMDBScore/', GetTopTenMoviesBasedOnIMDBScore.as_view()),
    url('GetLeastWatchedMovieBasedOnIMDBScore/', GetLeastWatchedMovieBasedOnIMDBScore.as_view()),
    url('GetMostWatchedGenre/', GetMostWatchedGenre.as_view()),
    url('GetMostPopularDirectorInFirstHundreadMovies/', GetMostPopularDirectorInFirstHundreadMovies.as_view()),
]
