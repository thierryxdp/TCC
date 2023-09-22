def retira_pontuacao(frase):
    ''' Essa função substitui todos os caracteres 
    de pontuação de uma determinada frase, str->str. '''
    f1 = frase.replace('-',' ')
    f2 = f1.replace(':',' ')
    f3 = f2.replace('.',' ')
    f4 = f3.replace(',',' ')
    f5 = f4.replace('!',' ')
    f6 = f5.replace('?',' ')
    f7 = f6.replace('...',' ')
    return f7