from flask import Flask

# Key will only need to be exposed once and can (and has to!) be deleted after that.
# openai.api_key=''

app = Flask(__name__)

from app import routes