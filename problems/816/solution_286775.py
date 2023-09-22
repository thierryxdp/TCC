def maiores(lista_inteiros,n):
    """
    Essa função dados uma lista com numeros inteiros e um numero n qualquer
    como argumentos, a função ira retornar somente os numeros da lista maiores que 'n'
    em ordem crescente
    """
    list.append(lista_inteiros,n)
    lista_ordenada = list.sort(lista_inteiros)
    index = list.index(lista_ordenada,n)
    lista = lista_ordenada[index:]
    
    return lista