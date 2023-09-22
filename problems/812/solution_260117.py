import re
def retira_pontuacao(frase):
    nfrase = re.sub('[!-.:-@]', ' ', frase)
    return nfrase