import re
import requests
import constants
import news
import dbmongo
from bs4 import BeautifulSoup
from googlesearch import search_news

class webScrapler:
    """Mi implementación de un web scrapler"""
    def __init__(self):
        self.data = []
        
    def busca(self,keywords):
        db = dbmongo.MongoDB()
        query = ""
        keywords.sort()
        keywords = [item.strip() for item in keywords]
        if db.exits_News(keywords) is True:
            return db.find_News(keywords)
       
        for word in keywords:
            query+=word+" "
        urls = search_news(query, lang = 'es', stop = 5)
        ans = {}
        ans['news'] = []
        for url in urls:
            print("Scrapling:",url)
            page = requests.get(url)
            texto = ""
            if page.status_code == 200:
                texto = self.get_news(page)
            aux = news.News(texto,0,str(url))
            ans['news'].append(aux.serialize_news()) 
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
                if len(ans) > 400:
                    return re.sub(r'(\n){1,}',' ', ans)
        return re.sub(r'(\n){2,}','\n', ans)
    
    def puntuacion(self,news):
        for txt in news:
            print(txt['score'])