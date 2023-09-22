def maiores(lista, n):
    '''função que retorna uma nova lista que contém apenas elementos
    maiores que 'n'.
    lista, int -> lista'''
    
    lista.sort()
    maior = []
    
    for i in range(len(lista)):
        if i < n:
            maior.clear(lista[i])
    lista = maior
            
    return lista