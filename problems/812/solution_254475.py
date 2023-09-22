def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuação são substituidos por espaço.
       str -> str'''
    s = frase
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    return frase