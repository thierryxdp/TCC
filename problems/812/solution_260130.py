def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase transformando as
    pontuações em espaços.
    str -> str'''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('...',' ')
    return frase