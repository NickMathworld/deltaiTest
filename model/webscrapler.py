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
        
    def find(self,keywords,language):
        db = dbmongo.MongoDB()
        query = ""
        #Tokenizamos por espacios en caso de que en una keyword vengan más de una palabra
        keywords = formatt.get_tokens(keywords)
        #Quitamos espacios en los caracteres
        keywords = formatt.drop_duplicates(keywords)
        # Checamos que si ya existen las keywords en algún request previo
        if db.exits_News(keywords,language) is True:
            return db.find_News(keywords,language)
       
        for word in keywords:
            query+=word+" "
        urls = search_news(query, lang = language, stop = CONTS.MAX_URLS)
        ans = {}
        ans['news'] = self.__get_content(urls)
        self.__get_top3(ans['news'],keywords)   
        
        #Guardamos el caso en la base de datos
        db.insert_News(ans,keywords,language)
        return ans

    def __get_content(self,urls):
        ans = []
        for url in urls:
            page = requests.get(url)
            txt = ""
            if page.status_code == CONTS.HTTP_ACCEPTED:
                txt = self.__get_news(page)
            if len(txt) == 0:
                continue
            aux = news.News(txt.strip(),1,str(url))
            ans.append(aux.serialize_news()) 
        return ans

    def __get_news(self,document):
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
    
    def __get_top3(self,news,keywords):
        sum = len(keywords)
        for word in keywords:
            for item in news:
                aux = algorithm.KMPSearch(word.lower(),item["content"].lower())
                sum = sum+aux
                item["ranking"]+=aux
        news.sort(reverse=True,key = self.__sort_news)
        for i in range(0, len(news)): 
            if i > 2:
                news.pop(3)
            else :
                 news[i]['ranking'] = news[i]['ranking']/sum

    def __sort_news(self,item):
        return item["ranking"]