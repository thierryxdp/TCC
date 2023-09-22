import re
def retira_pontuacao(frase):
    s = frase
print re.sub(r'[^\w\s]','',s)