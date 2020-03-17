import src.horoscope as horoscope
from datetime import datetime as dt


def generatePage(head, body):
    page = f"""<!DOCTYPE html>
<html>
    {head}
    {body}
</html>
"""
    return page


def generateHead(title):
    head = f"\t\t<meta charset='utf-8'>\n\t\t<title>{title}</title>\n"
    return f"<head>\n{head}\t</head>"


def generateBody(header, paragraphs):
    body = f"\t\t<h1>{header}</h1>\n"
    for p in paragraphs:
        body += f"\t\t<p>{p}</p>\n"
    body += f"\t\t<a href='about.html'>О реализации</a>"
    return f"<body>\n{body}\n\t</body>"


def generateAboutBody(header):
    body = f"\t\t<h1>{header}</h1>\n"
    body += f"\t\t<img src='https://ki.ill.in.ua/m/670x450/24482989.jpg' height=100 width=100/>\n"

    body += f"\t\t<ol>\n\t\t\t<li>Времена дня\n\t\t\t\t<ul>\n"
    for time in horoscope.times:
        body += f"\t\t\t\t\t<li>{time}</li>\n"
    body += f"\t\t\t\t</ul>\n\t\t\t</li>\n\t\t\t<li>Советы\n\t\t\t\t<ul>\n"
    for advice in horoscope.advices:
        body += f"\t\t\t\t\t<li>{advice}</li>\n"
    body += f"\t\t\t\t</ul>\n\t\t\t</li>\n\t\t\t<li>Обещания\n\t\t\t\t<ul>\n"
    for promise in horoscope.promises:
        body += f"\t\t\t\t\t<li>{promise}</li>\n"
    body += f"\t\t\t\t</ul>\n\t\t\t</li>\n\t\t</ol></br>\n"
    body += f"\t\t<a href='index.html'>Вернуться на главную</a>\n"
    return f"<body>\n{body}\t</body>"


def saveIndexPage(title, header, paragraphs, output="views/index.html"):
    file = open(output, 'w', encoding='utf-8')
    page = generatePage(head=generateHead(title),
                        body=generateBody(header=header, paragraphs=paragraphs))
    print(page, file=file)
    file.close()


def saveAboutPage(title, header, output="views/about.html"):
    file = open(output, 'w', encoding='utf-8')
    page = generatePage(head=generateHead(title),
                        body=generateAboutBody(header=header))
    print(page, file=file)


today = dt.now().date()
saveIndexPage(title="Гороскоп на сегодня",
              header="Что день " + str(today) + " готовит",
              paragraphs=horoscope.generateProphecies())

saveAboutPage(title=f"О гороскопе",
              header=f"&laquoО чём всё это&raquo")
