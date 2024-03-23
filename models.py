import random
import string
from flask import redirect
import redis
from config import Config

class RedisClient:
    
    counter=0
    
    def __init__(self):
        self.client = redis.Redis(host=Config.REDIS_URL, port=Config.REDIS_PORT, password=Config.REDIS_TOKEN, db=0, socket_timeout=5)
        ping = self.client.ping()
        if ping is True:
            print("Connected to redis")
        else:
            print("redis connection failed")
    def shorten_url(self, long_url):
        global counter
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(3)) + str(counter)
        counter += 1
        return short_url
        
        # Implementation for shortening URL

    def redirect_to_long_url(self, short_url):
        long_url = self.client.get(short_url)  # Retrieve long URL from Redis
        if long_url:
            return redirect(long_url.decode('utf-8'))
        else:
            return "URL not found", 404

        # Implementation for redirecting to long URL
