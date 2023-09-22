def maiores (lista,n):
    '''
    Função retorna todos os numeros maiores
    que o valor dado.
    list,int -> list
    '''
    lista.append(n+1)
    lista.sort()
    posicao = lista.index(n+1)
    return lista[posicao+1:]