def maiores(lista_numero, n):
    '''função que retorna uma nova lista que contém apenas elementos
    maiores que 'n'.
    lista, int -> lista'''
    
    lista_numero.sort()
    menor = []
    
    for i in range(len(lista_numero)):
        if i < n:
            menor.append(lista_numero[i])
    menor = lista_numero
    
    return menor