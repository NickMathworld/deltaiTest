class News:
    def __init__ (self,content,score,reference):
        self.content = content
        self.score = score
        self.reference = reference
    
    def serialize_news(self):
        ans = {}
        ans['content'] = self.content
        ans['ranking'] = self.score
        ans['reference'] = self.reference
        return ans