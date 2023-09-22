def filtraMultiplos(lista_numeros, n):
    """ Dada uma lista de números e um número, retorna 
    uma outra lista de números, com todos os numeros
    multiplos do número dado;
    list, float -> list"""
    a = lista_numeros
    i = 0
    lista = []
    while i < len(a):
        if(a[i] % n != 0):
            list.remove(lista, a[i])
            i = i + 1
    return lista