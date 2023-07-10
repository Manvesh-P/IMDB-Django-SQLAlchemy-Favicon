from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import (create_database,
                              database_exists)
from IMDBApp.models import Base
from logger_files.custom_logger import logger
from local_settings import my_credentials as settings


class SessionManager(object):

    def get_engine(self, user, password, host, port, database, *args, **kwargs):
        conn_str = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (user, password, host, port, database)
        print(conn_str)

        if not database_exists(conn_str):
            print('not exists')
            create_database(conn_str)
            print('database created')
            logger.info('database created')

        engine = create_engine(conn_str, pool_size=50, echo=True)
        logger.info('engine created')
        Base.metadata.create_all(engine)

        return engine


    def get_session(self, *args, **kwargs):

        engine = self.get_engine(*[settings[i] for i in settings])
        session = sessionmaker(bind=engine)

        return session


                             
