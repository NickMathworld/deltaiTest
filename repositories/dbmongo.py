from pymongo import MongoClient
class MongoDB:
    def insert_News(self,news,keywords):
        client = MongoClient(port=27017)
        db = client.deltAI
        aux = {'keywords':keywords,
                'news': news}
        result = db.webScrapler.insert_one(aux)
        return result.inserted_id
    
    def find_News(self,keywords):
        client = MongoClient(port=27017)
        db = client.deltAI
        news = db.webScrapler.find_one({'keywords':keywords})
        return news['news']
    
    def exits_News(self,keywords):
        client = MongoClient(port=27017)
        db = client.deltAI
        exist = db.webScrapler.find({'keywords':keywords}).count()
        return exist>0