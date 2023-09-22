import re 
def retira_pontuacao(s):
    out= re.sub(r'[^\w\s]','', s)
    return print(out)