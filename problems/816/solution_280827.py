def maiores(lista_numeros :list, n :int) -> list:
    """Dada uma lista de números inteiros e um número inteiro
    n, retorna outra lista que contém os números da lista dada
    maiores n."""
    
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    index_n = list.index(lista_numeros,n)
    tamanho = len(lista_numeros)
    
    return lista_numeros[index_n + 1 : tamanho]