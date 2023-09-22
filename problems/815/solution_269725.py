def insere(lista_numero,n):
    """função que dada na entrada uma lista ordenada crescente de números inteiros e um numero n, insira o n na posição correta;int,int-> int"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero