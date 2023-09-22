import re
def retira_pontuacao(frase):
    frase2 =re.sub('[,.!]','', frase)
    return frase2