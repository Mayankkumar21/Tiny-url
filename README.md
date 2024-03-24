# Tiny-url

### Check live demo of app
#### [Tiny-url-Demo](https://bitely.vercel.app)

### Running the project locally

  

```bash

https://github.com/Mayankkumar21/Tiny-url.git

```



 

### Install Python and pip

  

Visit https://www.python.org/downloads/

  

### Create virtual environment

  

```bash

python3 -m venv .venv

```

### Activate virtual Environment

  

```bash

source .venv/bin/activate

```

  

### Installing dependencies

  

```bash

pip3 install -r requirements. txt

```


### Installing Redis

Get more info on installing redis and redis server here https://redis.io/docs/install/install-redis/

  
### Setting up cloud Redis DB
Project is set to run on a cloud redis DB

Create your account at https://upstash.com/ for free cloud DB


### Set up environment variables

```bash

touch .env

```

```bash
Add REDIS_URL, REDIS_TOKEN, PORT IN .env file

```

If you get response as pong after ping then its successfully installed!

  

  

```bash

python3  app.py

```

And you are good to go!
