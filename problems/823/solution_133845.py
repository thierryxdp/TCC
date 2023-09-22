def faltante(lista_int: list)-> int:
    """Dada uma lista de números inteiros não repetidos de 1 a N, retorna
    qual o número inteiro que pertence ao intervalo [1,N], mas não pertence
    à lista de entrada."""
    
    list.sort(lista_int)
    comparador = list(range(1,lista_int[-1]))
    i = 0
    
    if (comparador == lista_int):
        if lista_int[0] != 1:
            return 1
        else:
            return lista_int[-1] + 1
    else:
        while (comparador[i] == lista_int[i] and i < len(lista_int)):
            i += 1

        return comparador[i]