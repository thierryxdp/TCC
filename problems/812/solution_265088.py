import re

def retira_pontuacao(frase):
    return re.sub(r'.|,', ' ', frase)