def retira_pontuacao(frase):
    '''
    retorna a mesma frase, com espacos no lugar das pontuacoes
    str -> str
    '''
    frase.replace('?',' '):
    frase.replace('—',' '):
    frase.replace(',',' '):
    frase.replace(':',' '):
    frase.replace(';',' '):
    frase.replace('.',' '):
    frase.replace('...',' '):
    return frase