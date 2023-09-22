def maiores(lista_numeros, n):
    '''Função que retorna uma lista que contém todos os números maiores
    que n da lista de entrada'''

    list.append(lista_numeros, n)
    
    list.sort(lista_numeros)
    
    a = list.index(lista_numeros, n)
    
    return lista_numeros[a+1:]