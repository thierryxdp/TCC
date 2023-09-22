def retira_pontuacao(frase):
    '''
    '''
    pontuacao= '-,:;.'
    for p in pontuacao :
        frase=frase.replace(p,' ')
        return frase