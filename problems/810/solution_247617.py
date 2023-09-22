def retira_pontuacao(texto):
    '''x'''
    a=str.replace(texto,',',' ')
    b=str.replace(a,'.',' ')
    c=str.replace(b,'-',' ')
    d=str.replace(c,'?',' ')
    e=str.replace(d,'!',' ')
    return e
def inverte(frase):
    '''x'''
    e=str.split(frase)
    return frase[::-1]