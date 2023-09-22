def maiores(lista_inteiros,n):
    """
    Essa função dados uma lista com numeros inteiros e um numero n qualquer
    como argumentos, a função ira retornar somente os numeros da lista maiores que 'n'
    em ordem crescente
    """
    lista_vazia = []
    lista_ordenada = list.sort(lista_inteiros)
    if n > lista_ordenada[-1]:
        return lista_vazia
    else:
        list.append(lista_inteiros,n)
        index = list.index(lista_ordenada,n)
        lista = lista_ordenada[index+1:]
    
    return lista