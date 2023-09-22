def faltante(lista_int: list)-> int:
    """Dada uma lista de números inteiros não repetidos de 1 a N, retorna
    qual o número inteiro que pertence ao intervalo [1,N], mas não pertence
    à lista de entrada."""
    
    list.sort(lista_int)
    comparador = list(range(1,lista_int[-1]))
    i = 0

    while (comparador[i] == lista_int[i]):
        i += 1

    return comparador[i]