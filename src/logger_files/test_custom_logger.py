import logging


_Format = '%(process)10s %(levelno)10s %(levelname)10s %(funcName)10s\
           %(threadName)10s %(asctime)10s %(msecs)10s %(message)10s'

logging.basicConfig(level=logging.DEBUG,
                    filename='logger_files/test_cases_tracker.log',
                    filemode='a',
                    datefmt='%H:%M:%S',
                    format=_Format)
logger = logging.getLogger(__name__)

