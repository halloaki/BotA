import os
from boto.s3.connection import S3Connection
BOT_PREFIX = "bota "

def index():
    TOKEN = str(os.environ.get('TOKEN'))
    return TOKEN

TOKEN = index()