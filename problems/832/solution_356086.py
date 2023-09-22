def eh_quadrada(a):
    '''função que, dada uma matriz, retorna True caso ela seja quadrada 
    e False caso não; list -> str'''
    matriz_vazia = [[]]
    if len(a)==len(a[0]):
         return True
    elif a == matriz_vazia:
        return True
    else:
        return False