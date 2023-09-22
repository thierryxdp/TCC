def maiores(lista,n):
    """Função que retorna outra lista com os números da lista de entrada maiores que o inteiro n
    list, int -> list"""
    
    lista_ordenada = lista + [n]
    lista_ordenada.sort()
    indice = lista_ordenada.index(n)
    
    return lista_ordenada[indice + 1:]