import re
def retira_pontuacao(frase):
    s = frase
out = s.sub(r'[^\w\s]','',s)
print(out)