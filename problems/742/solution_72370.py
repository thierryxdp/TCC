def substitui(s,x,i):
    '''funcao que retorna s exceto se x substituir i
    string,int,int-> string'''
    s = str(s)
    return s[:i] + x + s[i+1:]