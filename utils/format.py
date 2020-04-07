import re
def format_text(txt):
    ans = re.sub(r'(\n){1,}',' ', txt)
    ans = re.sub(r'(\t){1,}',' ', ans)
    ans = re.sub(r'(\r){1,}',' ', ans)
    ans = re.sub(r' {1,}',' ', ans)
    return ans

def get_tokens(keywords):
    ans = []
    for key in keywords:
        for word in key.split():
            ans.append(word)
    return ans
def drop_duplicates(keywords):
    keywords = [item.strip().lower() for item in keywords]
    keywords = list(set(keywords))
    keywords.sort()
    return keywords