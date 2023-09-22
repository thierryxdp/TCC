def retira_pontuacao (frase):
    '''Retira todos tipos de pontuação de uma frase, str->str'''
    frase = str.split (frase)
    return frase[0::-1]