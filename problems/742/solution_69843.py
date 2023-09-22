def substitui(s,x,i):
    """ Funcao que retorna uma string s que, dados um caractere x e um numero int i, substitua o i pelo caractere x.
    str,int,str->str
    s=str(s)"""
    return s[0:i] + str(x) + s[i+1:]