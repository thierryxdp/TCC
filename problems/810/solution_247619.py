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
    str.split(frase[::1])
    return frase