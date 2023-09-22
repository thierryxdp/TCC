def retira_pontuacao(frase):
    '''
    '''
    pontos = string.punctuation
    for c in pontos:
        frase = str.replace(c, '')
        return frase