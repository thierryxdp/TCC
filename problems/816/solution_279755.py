def maiores(lista_numero, n):
    '''função que retorna uma nova lista que contém apenas elementos
    maiores que 'n'.
    lista, int -> lista'''
    
    lista_numero.sort()
    maiores = []
    
    for i in range(len(lista_numero)):
        if lista[i] > n:
            maiores.append(lista_numero[i])
    lista_numero = maiores
            
    return lista_numero