import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    REDIS_URL=os.getenv("UPSTASH_REDIS_REST_URL")
    REDIS_TOKEN=os.getenv("UPSTASH_REDIS_REST_TOKEN")
    REDIS_PORT=os.getenv("PORT")
    print("Got envrionment variables",REDIS_PORT,REDIS_URL,REDIS_TOKEN)