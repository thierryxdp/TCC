import re
def retira_pontuacao(frase):
    l=re.sub(r'[^\w\s]','',frase)
    return l