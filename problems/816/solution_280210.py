def maiores(lista, n):
    '''Função que retorna todos os números de uma lista maior que "n" das informações "lista" = lista de números e "n" de entrada: list, int -> list'''
    
    if n not in lista:
        list.append(lista, n)
        
    list.sort(lista)
    indice = list.index(lista, n)
    
    fatiamento = lista[indice+1:]
    
    return fatiamento