import random
import time
from src.db import list_users, query_user_last_seen
from datetime import timedelta, datetime as dt


def check_user_is_active():
    attempts = 0
    email = input("Enter your email: ")
    while email.find("@") == -1:
        attempts += 1
        print("Incorrect email!", end=' ')
        if attempts >= 3:
            attempts = 0
            time.sleep(10)
        email = input("Try again: ")

    registered_users = list_users()
    login = email.split('@')[0].lower()
    newUser = True

    for user in registered_users:
        if user[0] == login:
            newUser = False
            lastSeen = query_user_last_seen(login)
            checkDate = lastSeen + timedelta(days=180)
            if dt.now() >= checkDate:
                print("You need confirm your login.")
            elif lastSeen < checkDate:
                availableDate = dt.now() + timedelta(days=180)
                print("Your account is available until", availableDate.date())
    if newUser:
        print("You are welcome!")


check_user_is_active()

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]

generated_prophecies = []
for i in range(0, 5):
    prophecy = str(times[random.randrange(0, len(times))]).capitalize() + \
               ' ' + str(advices[random.randrange(0, len(advices))]) + \
               ' ' + str(promises[random.randrange(0, len(promises))]) + '.'

    generated_prophecies.append(prophecy)
    print(generated_prophecies[i])
