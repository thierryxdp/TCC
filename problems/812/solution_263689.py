def retira_pontuacao(frase):
    '''
    '''
    pontuacao= p( '-',',',':',';',',')
    for p in pontuacao:
        frase=frase.replace(p.' ')
        return frase