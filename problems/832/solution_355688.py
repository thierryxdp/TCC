def eh_quadrada(a):
    """ Retorna True caso a seja uma matriz quadrada e false caso a não seja uma matriz quadrada; list -> bool"""
    matriz_vazia=[[]];
    if len(a)==len(a[0]):
        return True;
    else:
        if a==matriz_vazia:
            return True;
        if len(a)!=len(a[0]):
            return False;