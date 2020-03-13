import random

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
