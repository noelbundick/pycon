# Production settings
from .server import *

COMPRESS_ENABLED = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = env_or_default('ALLOWED_HOSTS', '').split(',')
REDIS_PASS = env_or_default('REDIS_PASS', '')

REDIS_LOCATION = '{}:6379'.format(REDIS_HOST)
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            REDIS_LOCATION
        ],
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': REDIS_PASS,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'PICKLE_VERSION': 2,
        },
    },
    SESSION_CACHE_ALIAS: {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            REDIS_LOCATION
        ],
        'OPTIONS': {
            'DB': 2,
            'PASSWORD': REDIS_PASS,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'PICKLE_VERSION': 2,
        },
    },
}
