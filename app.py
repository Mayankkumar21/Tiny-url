from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
import os
import string
import random
import redis
import sys

app = Flask(__name__)
load_dotenv()

REDIS_URL = os.getenv("UPSTASH_REDIS_REST_URL")
REDIS_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")
REDIS_PORT = os.getenv("PORT")

def redis_connect():
    try:
        client = redis.Redis(host=REDIS_URL, port=REDIS_PORT, password=REDIS_TOKEN, db=0, socket_timeout=5)
        ping = client.ping()
        if ping:
            print("Connection to Redis is successful")
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)

# Create client
redis_client = redis_connect()

def insert_url_to_cache(short_url: str, long_url: str) -> bool:
    try:
        # Store the long URL in Redis with a short URL as the key
        state = redis_client.set(short_url, long_url)
        return state
    except Exception as error:
        print(f"Error occurred: {error}")
        return False

def shorten_url(long_url):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if not redis_client.exists(short_url):  # Ensure short URL is unique
            # Ensure that the long URL is in absolute format
            if not long_url.startswith('http://') and not long_url.startswith('https://'):
                long_url = 'http://' + long_url
            success = insert_url_to_cache(short_url, long_url)
            if success:
                print(f"Successfully mapped {long_url} to {short_url}")
                return short_url


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = shorten_url(long_url)
        return render_template('home.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = redis_client.get(short_url)
    if long_url:
        print(long_url)
        print(long_url.decode('utf-8'))
        return redirect(long_url.decode('utf-8'))
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
