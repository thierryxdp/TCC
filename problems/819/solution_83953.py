def filtraMultiplos(lista,n):
    '''Retorna os multiplos de um numero n de uma determinada lista;
    list, int => lista'''
    i=0
    listafinal = [] 
    while i < len(lista):
        if (lista[i] % n) == 0:
            i=i+1
            return lista[i]