def retira_pontuacao(frase):
    '''substitui pontuacao por espaço.
    str -> str'''
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace('-', ' ')
    return frase