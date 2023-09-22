def retira_pontuacao(frase):
    index = 0
    frase.replace('!', ' ')
    frase.replace('?', ' ')
    frase.replace(',', ' ')
    frase.replace('.', ' ')
    frase.replace(';', ' ')
    frase.replace(':', ' ')
    frase.replace('-', ' ')
    return frase