import time
from UserActivities.db import list_users, query_user_last_seen
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
