def maiores(lista_numeros, n):
    '''Função que dada um números n e uma lista de números inteiros, retorne outra lista com apenas
    os números maiores que n e em ordem crescente
    list, int -> list'''
    list.append(lista_numeros, n)
    list.sort(lista_numeros)
    pos_de_n = list.index(lista_numeros, n)
    return lista_numeros[pos_de_n + 1:]