def retira_pontuacao(frase):
    frase = frase.replace('/', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('!', ' ')
    return frase
def inverte(frase):
    retira_pontuacao(frase)
    frase.split()
    frase.join()
    return frase[::-1]