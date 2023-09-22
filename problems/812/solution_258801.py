def retira_pontuacao(frase):
    index = 0
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace('-', ' ')
    return frase