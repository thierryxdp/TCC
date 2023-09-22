import re
def retira_pontuacao(frase):
    frase2 = re.sub("[,.!]","")
    return frase2