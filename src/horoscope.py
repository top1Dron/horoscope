import random


def generate_prophecies(total_num=5):
    times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
    advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
    promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
                "неожиданного праздника", "приятных перемен"]

    generated_prophecies = []
    for i in range(0, 5):
        time = random.choice(times)
        advice = random.choice(advices)
        promise = random.choice(promises)
        prophecy = time.capitalize() + ' ' + advice + ' ' + promise + '.'
        generated_prophecies.append(prophecy)

    return generated_prophecies
