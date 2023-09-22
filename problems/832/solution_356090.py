def eh_quadrada(a):
    '''função que, dada uma matriz a, retorna True caso ela seja quadrada 
    e False caso não; list -> str'''
    if len(a) == len(a[0]):
         return True
    elif a == []:
        return True
    else:
        return False