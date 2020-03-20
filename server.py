from bottle import route, run, view, static_file, get
from datetime import datetime as dt
import os

from src.horoscope import generateProphecies
import random


@get("/static/scripts/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./scripts")


@route("/")
@view("prophecies")
def index():
    now = dt.now()
    specialDate = random.random()
    return {
        "date": f"{now.year}-{now.month}-{now.day}",
        "prophecies": generateProphecies(),
        "specialDate": specialDate
    }


@route("/about")
@view("about")
def about():
    pass


@route("/api/forecasts")
def api_forecasts():
    return {
        "prophecies": generateProphecies(total_num=5, num_sentences=2)
    }

if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host='0.0.0.0', port = int(os.environ.get("PORT" ,5000)))
    else:
        run(
            host="localhost",
            port=8000,
            debug=True
        )
