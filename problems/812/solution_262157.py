def retira_pontuacao(frase):
    '''
    retira pontuacoes da frase e retorna espaco no lugar
    str -> str
    '''
    frase.replace('—',' ')
    frase.replace('?',' ')
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace('.',' ')
    frase = frase.replace('...',' ')+frase.replace('.',' ')+frase.replace(';',' ')+frase.replace(':',' ')
    return frase