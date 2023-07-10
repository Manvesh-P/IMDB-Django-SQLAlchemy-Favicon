from django.shortcuts import render
from rest_framework.views import APIView
from sqlalchemy.exc import (IntegrityError,
                            InterfaceError,
                            OperationalError,
                            ArgumentError,
                            ProgrammingError)
import sys
import psycopg2
print('psycopg2 imported successfully')
from session_maker import SessionManager
print('session maker returned session')
from logger_files.custom_logger import logger
from ActualLogic import ActualLogicServer
# Create your views here.

session = SessionManager().get_session()
print('session created')

class InsertMoviesData(APIView):
    def post(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')

            print('****************about call function**********************')

            res = ActualLogicServer().insert_movies_data(session_obj, request.data)

        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except (IntegrityError, InterfaceError, OperationalError, ProgrammingError, ArgumentError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            logger.error((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')

        else:
            l.append(res)
            logger.debug(res)
            session_obj.commit()
            logger.info('session committed')

        finally:
            with open('templates/template_1.html', mode='w', encoding='utf-8') as f:
                f.write('<!doctype html>\n<html>\n<body><p><font color = #FF0000>' + str(l) + '</font></p>\n</html>')

            session_obj.close()
            logger.info('session closed')

            return render(request, 'template_1.html', {})


class GetDirectorWithMaxNumberOfMovies(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = ActualLogicServer().get_director_with_max_number_of_movies(session_obj)

            with open('href_file.txt', mode='r') as f1:
                data = f1.read()


        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except (IntegrityError, InterfaceError, ArgumentError, OperationalError, ProgrammingError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            logger.error((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')

        else:
            l.append(res)
            logger.debug(res)
            session_obj.commit()
            logger.info('session committed')

        finally:
            with open('templates/template_2.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'IMDB' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'The director with more number of films is/are: ' + '<font color = #00FF00>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')

            return render(request, 'template_2.html', {})


class GetTopTenMoviesBasedOnIMDBScore(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = ActualLogicServer().get_top_ten_movies_based_on_imdb_score(session_obj)

            with open('href_file.txt', mode='r') as f1:
                data = f1.read()

        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except (IntegrityError, InterfaceError, ArgumentError, OperationalError, ProgrammingError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            logger.error((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')

        else:
            l.append(res)
            logger.debug(res)
            session_obj.commit()
            logger.info('session committed')

        finally:
            with open('templates/template_3.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'IMDB' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'Top ten movies based on imdb score are: ' + '<font color = #0000FF>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')

            return render(request, 'template_3.html', {})


class GetLeastWatchedMovieBasedOnIMDBScore(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = ActualLogicServer().get_least_watched_movie_based_on_imdb_score(session_obj)
            print('*********************')

            with open('href_file.txt', mode='r') as f1:
                data = f1.read()

        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except (IntegrityError, InterfaceError, OperationalError, ArgumentError, ProgrammingError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            logger.error((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')

        else:
            l.append(res)
            logger.debug(res)
            session_obj.commit()
            logger.info('session committed')

        finally:
            with open('templates/template_4.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<html>\n<title>' + 'IMDB' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'The least watched movie(s) based on imdb score is/are: ' + '<font color = #FFFF00>' + str(l) +
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')

            return render(request, 'template_4.html', {})

class GetMostWatchedGenre(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            res = ActualLogicServer().get_most_watched_genre(session_obj)

            with open('href_file.txt', mode='r') as f1:
                data = f1.read()

        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except (IntegrityError, InterfaceError, OperationalError, ArgumentError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except Exception as ex:
            l.append((type(ex), sys.excx_info()[1], sys.exc_info()[2]))
            logger.error((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')

        else:
            l.append(res)
            logger.debug(res)
            session_obj.commit()
            logger.info('session committed')

        finally:
            with open('templates/template_5.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'IMDB' + '</title>\n</html>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' + 
                        '<body><p>' + 'The most watched genre(s) is/are: ' + '<font color = #00FFFF>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')

            return render(request, 'template_5.html', {})

class GetMostPopularDirectorInFirstHundreadMovies(APIView):
    def get(self, request):
        l = []
        try:
            session_obj = session()
            logger.info('session started')
            print('*****************')
            res = ActualLogicServer().get_most_popular_director_in_first_hundread_movies(session_obj)
            print('88888888888888888888888888888888888')

            with open('href_file.txt', mode='r') as f1:
                data = f1.read()

        except (ImportError, NameError, TypeError, AttributeError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except (IntegrityError, InterfaceError, ArgumentError, ProgrammingError, OperationalError):
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except psycopg2.OperationalError:
            l.append(sys.exc_info())
            logger.error(sys.exc_info())
            session_obj.rollback()
            logger.info('session rolled back')

        except Exception as ex:
            l.append((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            logger.error((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
            session_obj.rollback()
            logger.info('session rolled back')

        else:
            l.append(res)
            logger.debug(res)
            session_obj.commit()
            logger.info('session committed')

        finally:
            with open('templates/template_6.html', mode='w', encoding='utf-8') as f:
                f.write('{% load static %}\n<!doctype html>\n<html>\n<head>\n<title>' + 'IMDB' + '</title>\n</head>\n' + 
                        '<link rel="icon" href=' + '"' + data + '"' + ' type="image/x-icon"/>\n' +
                        '<body><p>' + 'The most popular director in first hundread movies is/are: ' + '<font color = #FF00FF>' + str(l) + 
                        '</font></p></body>\n</html>')
            session_obj.close()
            logger.info('session closed')

            return render(request, 'template_6.html', {})



        

