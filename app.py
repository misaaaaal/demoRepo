from flask import Flask
import os
app = Flask(__name__)
env_var=os.getenv('ENV_VAR')

@app.route('/')
def home():
    return f'<h1>Im original: {env_var}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
