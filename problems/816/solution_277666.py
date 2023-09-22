def maiores(lista, n ):
    """funcao que retorna uma lista contendo os numeros da primeira lista
       maiores que n
       
       lista, int-> lista
    """"

    list.sort(lista)
    list.insert(lista,n)
    posicao_de_n = list.index(lista,n)
    
    return lista[posicao_de_n:]