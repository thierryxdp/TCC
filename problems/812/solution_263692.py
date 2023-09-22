def retira_pontuacao(frase):
    '''
    '''
    pontuacao= p( '-',',',':',';',',')
    if p in pontuacao:
        frase=frase.replace(p,' ')
        return frase