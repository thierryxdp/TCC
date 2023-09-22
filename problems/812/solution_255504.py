import re
def retira_pontuacao(frase):
    s = frase
    saida = s.sub(r'[^\w\s]','',s)
    return saida