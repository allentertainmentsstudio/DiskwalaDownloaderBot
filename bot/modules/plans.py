import time

user_plans = {}

def get(user):
    p = user_plans.get(user, {"plan":"FREE","expiry":0})
    if p["expiry"] < time.time():
        return "FREE"
    return p["plan"]

def add(user, days):
    user_plans[user] = {
        "plan":"PREMIUM",
        "expiry": time.time() + days*86400
    }

def remove(user):
    user_plans[user] = {"plan":"FREE","expiry":0}
