def retira_pontuacao(frase):
    '''
    '''
    pontuacao= '-,:;.'
    for pontuacao in frase :
        frase=frase.remove(pontuacao,' ')
        
        return frase