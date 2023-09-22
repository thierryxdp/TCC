def retira_pontuacao(frase):
    '''
    '''
    pontuacao= '-,:;.'
    for p in pontuacao :
        frase=str.replace(p,' ')
        return frase