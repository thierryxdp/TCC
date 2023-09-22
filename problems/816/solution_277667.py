def maiores(lista, n ):
    """funcao que retorna uma lista contendo os numeros da primeira lista
       maiores que n
       
       lista, int-> lista
    """"

    list.append(lista,n)
    list.sort(lista)
    posicao_de_n = list.index(lista,n)
    
    return lista[posicao_de_n:]