def substitui(s,x,i):
    '''retorna s exceto se x substituir i'''
    s=str(s)
    return s[:1] + x + s[i+1:]