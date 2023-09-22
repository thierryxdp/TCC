def eh_quadrada(a):
    """ Retorna True caso a seja uma matriz quadrada e false caso a não seja uma matriz quadrada; list -> bool"""
    if len(a)==len(a[0]) or a==[]:
        return True;
    else:
        return False;