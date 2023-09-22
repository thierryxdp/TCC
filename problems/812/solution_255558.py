import re
def retira_pontuacao(frase):
    s = frase
    out = re.math(r'[^\w\s]','',s)
print('out')