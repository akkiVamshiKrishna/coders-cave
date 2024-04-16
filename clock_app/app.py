from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_time():
    return get_current_time()

if __name__ == '__main__':
    app.run(debug=True)
