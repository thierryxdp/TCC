def maiores (lista_numeros, n):
    '''Função retorna todos os números maiores que n contidos na lista de números dada.;
    list, int -> list'''
    list.append (lista_numeros, n)
    list.sort (lista_numeros)
    posicao = list.index (lista_numeros, n)
    return lista_numeros [posicao+1:]