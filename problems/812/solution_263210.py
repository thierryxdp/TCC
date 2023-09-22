retira_pontuacao (frase):
    '''
    str -> str
    '''
    pontos = ['-',',',':',';','!','?','.','...']
    return frase.replace(pontos,' ')