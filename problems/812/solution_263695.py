def retira_pontuacao(frase):
    '''
    '''
    pontuacao= p( '-',',',':',';',',')
    if pontuacao in frase :
        frase=frase.replace(pontuacao,' ')
        return frase