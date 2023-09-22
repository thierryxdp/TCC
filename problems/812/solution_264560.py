def retira_pontuacao(frase):
    ''' Essa função substitui todos os caracteres 
    de pontuação de uma determinada frase, str->str. '''
    f1 = frase.replace('-',' ')
    f2 = frase.replace(':',' ')
    f3 = frase.replace('.',' ')
    f4 = frase.replace(',',' ')
    f5 = frase.replace('!',' ')
    f6 = frase.replace('?',' ')
    f7 = frase.replace('...',' ')
    return f7