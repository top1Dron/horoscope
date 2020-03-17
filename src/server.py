from bottle import route, run, view, static_file, get
from datetime import datetime as dt
import sys
sys.path.insert(0, '../src')
from horoscope import generateProphecies
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


@route("/api/forecasts")
def api_forecasts():
    return {
        "prophecies": generateProphecies(total_num=6, num_sentences=2)
    }


run(
    host="localhost",
    port=8000,
    debug=True
)
