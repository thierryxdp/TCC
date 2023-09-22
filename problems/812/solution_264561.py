def retira_pontuacao(frase):
    ''' Essa função substitui todos os caracteres 
    de pontuação de uma determinada frase, str->str. '''
    f1 = frase.replace('-',' ')
    f2 = f1replace(':',' ')
    f3 = f2replace('.',' ')
    f4 = f3replace(',',' ')
    f5 = f4replace('!',' ')
    f6 = f5replace('?',' ')
    f7 = f6replace('...',' ')
    return f7