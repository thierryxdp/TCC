def maiores(lista,n):
    """dada uma lista de numeros inteiros e um número 
    inteiro n , ela retorna uma lista apenas com os numeros maiores 
    que n
    list, str-> list"""
    list.append(lista,n)
    list.sort(lista)
    indice=list.index(lista,n)
    retornar=lista[indice:]
    return retornar