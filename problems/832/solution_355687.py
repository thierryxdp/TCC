def eh_quadrada(a):
    """ Retorna True caso a seja uma matriz quadrada e false caso a não seja uma matriz quadrada; list -> bool"""
    if len(a)==len(a[0]):
        return True;
    else:
        if a==[[]]:
            return True;
        if len(a)!=len(a[0]):
            return False;