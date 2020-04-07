import utils.format as formatt
import utils.constants as CONTS
import model.news as news
import utils.algorithm as algorithm
import repositories.dbmongo as dbmongo

import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search_news

class WebScrapler:
    """Mi implementación de un web scrapler"""
    def __init__(self):
        self.data = []
        
    def find(self,keywords):
        db = dbmongo.MongoDB()
        query = ""
        keywords.sort()
        keywords = [item.strip() for item in keywords]
        # Checamos que si ya existen las keywords en algún request previo
        if db.exits_News(keywords) is True:
            return db.find_News(keywords)
       
        for word in keywords:
            query+=word+" "
        urls = search_news(query, lang = 'es', stop = CONTS.MAX_URLS)
        ans = {}
        ans['news'] = []
        for url in urls:
            page = requests.get(url)
            txt = ""
            if page.status_code == CONTS.HTTP_ACCEPTED:
                txt = self.get_news(page)
            if len(txt) == 0:
                continue
            aux = news.News(txt.strip(),1,str(url))
            ans['news'].append(aux.serialize_news()) 
        self.get_top3(ans['news'],keywords)   
        #Guardamos el caso en la base de datos
        db.insert_News(ans,keywords)
        return ans


    def get_news(self,document):
        soup = BeautifulSoup(document.content, 'html.parser')
        for tag in soup.find_all(["script","style"]):
            tag.decompose()
        paragraphs = soup.find_all("p")
        ans = ""
        tags = re.compile(r'<.*?>')
        for paragraph in paragraphs:
            for subp in paragraph.contents:
                ans+=tags.sub("",str(subp))+"\n"
                if len(ans) > CONTS.MAX_NEW:
                    return formatt.format_text(ans)
        return formatt.format_text(ans)
    
    def get_top3(self,news,keywords):
        sum = len(keywords)
        for word in keywords:
            for item in news:
                aux = algorithm.KMPSearch(word.lower(),item["content"].lower())
                sum = sum+aux
                item["score"]+=aux
        news.sort(reverse=True,key = self.sort_news)
        for i in range(0, len(news)): 
            if i > 2:
                news.pop(3)
            else :
                 news[i]['score'] = news[i]['score']/sum

    def sort_news(self,item):
        return item["score"]