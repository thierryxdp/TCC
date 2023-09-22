def maiores(lista_inteiros,n):
    """
    Essa função dados uma lista com numeros inteiros e um numero n qualquer
    como argumentos, a função ira retornar somente os numeros da lista maiores que 'n'
    em ordem crescente
    """
    lista_vazia = []
    list.sort(lista_inteiros)
    lista_ordenada = lista_inteiros
    if n > lista_inteiros[-1]:
        return lista_vazia
    
    else:
        list.append(lista_ordenada,n)
        list.sort(lista_ordenada)
        index = list.index(lista_ordenada,n)
        lista = lista_ordenada[index+1:]
    
    return lista