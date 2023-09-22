def eh_quadrada(a):
    """ Retorna se a matriz a é quadrada ou não; list -> bool"""
    if a==[]:
        return True;
    elif len(a)==len(a[0]):
        return True;
    else:
        return False;