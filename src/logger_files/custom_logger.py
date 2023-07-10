import logging


_FORMAT = '%(process)10s %(levelno)5d %(levelname)10s %(funcName)10s\
           %(threadName)10s %(asctime)10s %(msecs)10s %(message)10s'

logging.basicConfig(level=logging.DEBUG,
                    filename='logger_files/tracker.log',
                    filemode='a',
                    datefmt='%H:%M:%S',
                    format=_FORMAT)
logger = logging.getLogger(__name__)


