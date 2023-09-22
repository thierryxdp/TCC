def retira_pontuacao(frase):
    '''
    retorna a mesma frase, com espacos no lugar das pontuacoes
    str -> str
    '''
    frase=frase.replace('...',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(':',' ')
    return frase