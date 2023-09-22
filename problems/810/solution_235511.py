def retira_pontuacao(frase):
    return frase.replace('.', ' ').replace('?', ' ').replace('!', ' ').replace(',', ' ').replace('-', ' ').replace(':', ' ').replace(':', ' ').replace(';', ' ').replace('...', ' ')

def inverte(frase):
    return retira_pontuacao(frase).split()[::-1].join(' ')