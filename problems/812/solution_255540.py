import re
def retira_pontuacao(frase):
    s = frase
out = re.sub(r'[^\w\s]','',s)
print(out)