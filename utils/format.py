import re
def format_text(txt):
    ans = re.sub(r'(\n){1,}',' ', txt)
    ans = re.sub(r'(\t){1,}',' ', ans)
    ans = re.sub(r'(\r){1,}',' ', ans)
    ans = re.sub(r' {1,}',' ', ans)
    return ans