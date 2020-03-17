import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generateProphecies(total_num=5, num_sentences=3):
    generatedProphecies = []
    for generateProphecy in range(total_num):
        prophecy = ""
        for sentence in range(num_sentences):
            time = random.choice(times)
            advice = random.choice(advices)
            promise = random.choice(promises)
            prophecy += time.capitalize() + ' ' + advice + ' ' + promise + '.'
            if generateProphecy != 2:
                prophecy += ' '
        generatedProphecies.append(prophecy)

    return generatedProphecies
