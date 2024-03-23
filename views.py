from flask import render_template
from models import RedisClient

redis_client = RedisClient()

def shorten_url(long_url):
    short_url = redis_client.shorten_url(long_url)
    return short_url

def redirect_to_long_url(short_url):
    long_url = redis_client.redirect_to_long_url(short_url)
    return long_url
