from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!' + '\n'

@app.route('/time')
def get_time():
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern)
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z') + '\n'


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
