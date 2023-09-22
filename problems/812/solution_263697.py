def retira_pontuacao(frase):
    '''
    '''
    pontuacao= '-,:;.'
    for pontuacao in frase :
        frase=frase.replace(pontuacao,' ')
        return frase