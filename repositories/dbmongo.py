from pymongo import MongoClient
class MongoDB:
    def insert_News(self,news,keywords,language):
        client = MongoClient("mongodb+srv://nick:123@deltaicluster-072dm.mongodb.net/test?retryWrites=true&w=majority")
        db = client.deltAI
        aux = {'keywords':keywords,
                'news': news,
                'language':language}
        result = db.webScrapler.insert_one(aux)
        return result.inserted_id
    
    def find_News(self,keywords,language):
        client = MongoClient("mongodb+srv://nick:123@deltaicluster-072dm.mongodb.net/test?retryWrites=true&w=majority")
        db = client.deltAI
        news = db.webScrapler.find_one({'keywords':keywords,'language':language})
        return news['news']
    
    def exits_News(self,keywords,language):
        client = MongoClient("mongodb+srv://nick:123@deltaicluster-072dm.mongodb.net/test?retryWrites=true&w=majority")
        db = client.deltAI
        exist = db.webScrapler.find({'keywords':keywords,'language':language}).count()
        return exist>0