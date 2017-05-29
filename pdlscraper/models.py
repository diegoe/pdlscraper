import dataset

from pdlscraper import settings


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    :param test: if test is True then create an empty test database
    """
    database = [
        settings.DATABASE['drivername'],
        '//' + settings.DATABASE['username'],
        settings.DATABASE['password'] + '@' + settings.DATABASE['host'],
        settings.DATABASE['port'] + '/' + settings.DATABASE['database'],
    ]
    db = dataset.connect(':'.join(database))

    return db
