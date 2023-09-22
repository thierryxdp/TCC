def retira_pontuacao(frase):
    '''
    retira pontuacoes da frase e retorna espaco no lugar
    str -> str
    '''
    return frase.replace(('?',' ')'.',' ')