def maiores (lista_numero, n):
    """recebe uma lista de numeros inteiros e um outro inteiro n, e retorna
    uma lista contendo todos os elementos da lista origial maiores do que n
    list, int -> list"""
    
    lista_numero = lista_numero + [n]
    
    lista_numero = sorted(lista_numero)
    
    x = list.index(lista_numero, n)
    
    return lista_numero[(x+1):len(lista_numero)]