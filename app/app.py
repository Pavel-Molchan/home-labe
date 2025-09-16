from flask import Flask, render_template
import os

app = Flask(__name__)

db_host = os.environ.get('DB_HOST', 'localhost')
app_version = os.environ.get('APP_VERSION', 'v1.0.0')

@app.route('/')
def index():
    """
    Обрабатывает запросы к главной странице ('/').
    """
    return render_template('index.html', version=app_version, db_host=db_host)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)