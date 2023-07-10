from IMDBApp.models import IMDB
from collections import defaultdict


class ActualLogicServer(object):
    def insert_movies_data(self, session_obj, _data, *args, **kwargs):
        for rec in _data:
            session_obj.add(
                            IMDB(_id = rec['_id']['$oid'],
                                popularity = rec['99popularity'],
                                director = rec['director'],
                                genre = rec['genre'],
                                imdb_score = rec['imdb_score'],
                                name = rec['name'])
                            )
            session_obj.commit()

        return 'Data inserted successfully'

    def get_director_with_max_number_of_movies(self, session_obj, *args, **kwargs):
        res = session_obj.query(IMDB).all()
        
        if res:
            movie_dict = dict([(j.director, [i.director for i in res].count(j.director)) for j in res])
            print(movie_dict)
            max_rec = max(movie_dict.items(), key=lambda x: x[1])
            return [i for i in movie_dict if movie_dict[i] == max_rec[1]]
        else:
            return 'No data found'

    def get_top_ten_movies_based_on_imdb_score(self, session_obj, *args, **kwargs):
        res = session_obj.query(IMDB).all()
        return sorted(dict([(rec.name, rec.imdb_score) if [rec1.name for rec1 in res].count(rec.name) == 1 else (rec.name + ' directed by--> ' + rec.director, rec.imdb_score) for rec in res]).items(), key=lambda x: x[1], reverse=True)[:10] if res else 'No data found'

    def get_least_watched_movie_based_on_imdb_score(self, session_obj, *args, **kwargs):
        res = session_obj.query(IMDB).all()

        print('***********************')
        if res:
            movie_dict = dict([(rec.name, rec.imdb_score) if [rec1.name for rec1 in res].count(rec.name) == 1 else (rec.name + ' directed by-->' + rec.director, rec.imdb_score) for rec in res])
            print(movie_dict)
            min_rec = min(movie_dict.items(), key=lambda x: x[1])
            return [i for i in movie_dict if movie_dict[i] == min_rec[1]]
        else:
            return 'No data found'

    def get_most_watched_genre(self, session_obj, *args, **kwargs):
        res = session_obj.query(IMDB).all()
        
        if res:
            genre_dict = eval('{' + ','.join([str({rec1.strip(): ','.join([','.join([rec3.strip() for rec3 in rec2.genre]) for rec2 in res if rec2.genre]).split(',').count(rec1.strip()) for rec1 in rec.genre}).replace('{', '').replace('}', '') for rec in res if rec.genre]) + '}')
            print(genre_dict)
            max_rec = max(genre_dict.items(), key=lambda x: x[1])
            return [i for i in genre_dict if genre_dict[i] == max_rec[1]]
        else:
            return 'No data found'

    def get_most_popular_director_in_first_hundread_movies(self, session_obj, *args, **kwargs):
        res = session_obj.query(IMDB).all()
        if res:
            d = dict([(rec.director, sum([rec1.popularity for ind1, rec1 in enumerate(res) if rec1.director == rec.director and ind1 < 100])/len([rec3.popularity for ind3, rec3 in enumerate(res) if ind3 < 100 and rec3.director == rec.director])) for ind, rec in enumerate(res) if ind < 100])
            print(d)
            max_rec = max(d.items(), key=lambda x: x[1])
            list_max_rec = [i for i in d if d[i] == max_rec[1]]

            return list_max_rec
        else:
            return 'No data found'

