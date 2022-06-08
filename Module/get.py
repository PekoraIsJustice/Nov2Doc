
from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
from docx import Document
import progressbar
from Module import check

docs = Document()

def toDoc(par, style='Body Text'):
    docs.add_paragraph(par, style=style)

def getContent(url):
    chapList = requests.get(url)
    chapList = BeautifulSoup(chapList.text, 'lxml')
    chapList = chapList.find("div", {"class" : "widget-episodeBody js-episode-body"})
    chapList = chapList.find_all("p")
    for item in chapList:
        toDoc(item.contents[0],)

def loop(pack, tL):
    bar = progressbar.ProgressBar(max_value=tL)
    for i, item in enumerate(pack):
        if item.find("a") != None:
            toDoc(item.a.span.text, 'Heading 2')
            toDoc(item.a.time.text)
            getContent("https://kakuyomu.jp" + item.a['href'])
            bar.update(i)
        else :
            toDoc(item.span.text, 'Heading 1')
            bar.update(i)

def getNovel(_url, nsp):
    url = _url
    cont = requests.get(url)
    cont = BeautifulSoup(cont.text, 'lxml')
    info = cont.find(id="workHeader-inner")
    title =info.h1.text
    author = info.h2.select("span")[1].text
    cont = cont.main
    cont = cont.find(id="table-of-contents")
    ctime = cont.header.div.select("p")[1].time['datetime'][:10]
    ctime = ctime.replace('-','')

    if check.chkUpdate(ctime, nsp, title):
        print("Already update to latest.")
        return None, None

    cont = cont.find_all("li")
    totL = len(cont)
    
    loop(cont, totL)
    
    name = title + '_' + author + '_' + ctime

    return name, docs