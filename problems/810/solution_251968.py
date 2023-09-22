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
    frase = str.split (frase)
    frase = frase[::-1]
    return frase