import re
def retira_pontuacao(frase):
    frase2 = re.sub("[^A-Za-z]","",frase)
    return frase2