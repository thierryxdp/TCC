def retira_pontuacao(frase):
    '''
    '''
    pontos = str.punctuation
    for c in pontos:
        frase = str.replace(c, '')
        return frase