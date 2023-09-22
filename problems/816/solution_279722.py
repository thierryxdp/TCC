def maiores(lista_numero, n):
    '''função que retorna uma nova lista que contém apenas elementos
    maiores que 'n'.
    lista, int -> lista'''
    
    lista_numero.sort()
    menor = []
    
    for i in range(len(lista_numero)):
        if i < n:
            menor.remove(lista_numero[i])
    return menor