def retira_pontuacao (frase):
    '''Retira todos tipos de pontuação de uma frase, str->str'''
    frase = frase.replace ('.', ' ')
    frase = frase.replace (',', ' ')
    frase = frase.replace ('-', ' ')
    frase = frase.replace (':', ' ')
    frase = frase.replace (';', ' ')
    frase = frase.replace ('?', ' ')
    frase = frase.replace ('!', ' ')
    return frase

def inverte (frase):
    frase = retira_pontuacao (frase)
    return frase [0::-1]