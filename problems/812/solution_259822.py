def retira_pontuacao(frase):
    '''ao receber uma frase, retorna a mesma frase,
    porém sem pontuação.
    str -> str'''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('...',' ')
    return frase