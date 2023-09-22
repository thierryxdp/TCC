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

def inverte(frase):
    ''' Essa função recebe uma frase de entrada e retorna a mesma
    com as palavras na ordem inversa, sem letras maiúsculas e sem pontuação,
    str->str. '''
    f1 = frase.lower( )
    f2 = retira_pontuacao(f1)
    f3 = f2.split( )
    f4 = f3[::-1]
    f5 = str.join(' ',f4)
    return f5