def retira_pontuacao (frase):
    '''Retira todos tipos de pontuação de uma frase, str->str'''
    frase = frase.replace ('.', ' ')
    frase = frase.replace (',', ' ')
    return frase