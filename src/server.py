from bottle import route, run, view
from datetime import datetime as dt
import random


@route("/")
@view("prophecies")
def index():
    now = dt.now()
    specialDate = random.random()
    return {"date": f"{now.year}-{now.month}-{now.day}",
            "prophecies": [
                "Перед сном будьте открыты для неожиданного праздника.",
                "Днём будьте открыты для гостей из забытого прошлого.",
                "Днём ожидайте приятных перемен.",
                "Днём ожидайте гостей из забытого прошлого.",
                "Днём предостерегайтесь гостей из забытого прошлого."
            ],
            "specialDate": specialDate}


@route("/api/test")
def api_test():
    return {"test": True}


run(
    host="localhost",
    port=8000,
    debug=True
)
