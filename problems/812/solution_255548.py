import re
def retira_pontuacao(frase):
    s = frase
out = r.sub(r'[^\w\s]','',s)
print(out)