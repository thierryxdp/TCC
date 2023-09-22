def filtraMultiplos (lista,numeroN):
    ''' Funcao que dado uma lista e um numero como parametro, retorna uma nova lista
contendo todos os numeros multiplos do numeroN presentes na lista.
    list + int -> list '''
    divisiveis = ()
    posicao = 0

    while posicao < len(lista):
        if lista[posicao]%numeroN==0:
            divisiveis = [lista[posicao]]
        posicao = posicao + 1
            
    return divisiveis