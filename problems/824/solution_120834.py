def uppCons(x):
    """Esta função recebe uma string e torna maiuscula as consoante.
    assinatura str -> str
    """ 
    a = ''
    for c in x:
        if c in 'bcdfghjklmnpqrtvxwzç':
            a +=str.upper(c)
        else:
            a + = c
            return a