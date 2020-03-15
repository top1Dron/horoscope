import random


def generateProphecies(total_num=5):
    times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
    advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
    promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
                "неожиданного праздника", "приятных перемен"]

    generatedProphecies = []
    for i in range(0, 5):
        time = random.choice(times)
        advice = random.choice(advices)
        promise = random.choice(promises)
        prophecy = time.capitalize() + ' ' + advice + ' ' + promise + '.'
        generatedProphecies.append(prophecy)

    return generatedProphecies
