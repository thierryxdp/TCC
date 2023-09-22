def maiores(lista,n):
    '''Retorna uma lista de numeros maiores que n, baseada
       na lista dada como argumento;
       list, int -> list'''
    
    lista.sort()
    
    return lista[n:]