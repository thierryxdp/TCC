def maiores(lista, n):
    '''Recebe uma lista (lista) e um número inteiro(n),
    retorna uma lista com todos os números maiores que n
    em ordem crescente
    
    list, int -> list
    '''
    
    if n in lista:
        list.sort(lista)
        lista1 = lista[list.index(lista, n)+1:]
        
        return lista1
    else:
        lista.insert(-1, n)
        list.sort(lista)
        lista1 = lista[list.index(lista, n)+1:]
        
        return lista1