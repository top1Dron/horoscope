from src.horoscope import generateProphecies
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
    return f"<body>\n{body}\t</body>"


def savePage(title, header, paragraphs, output="index.html"):
    file = open(output, 'w', encoding='utf-8')
    page = generatePage(head=generateHead(title),
                        body=generateBody(header=header, paragraphs=paragraphs))
    print(page, file=file)
    file.close()


today = dt.now().date()
savePage(title="Гороскоп на сегодня",
         header="Что день " + str(today) + " готовит",
         paragraphs=generateProphecies())
