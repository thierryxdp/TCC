def retira_pontuacao(frase):
    frase = frase.replace('/', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('!', ' ')
    def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = frase.split()
    frase = frase[::-1]
    frase = ''.join(frase)
    return frase