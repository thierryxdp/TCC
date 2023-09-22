def maiores(lista_numeros,n):
    """ Essa função recebe como parâmetro de entrada uma lista
    de números inteiros e um número inteiro n. Posto isso, essa
    função retornará outra lista contendo todos os números da 
    lista original que sejam maiores que n, sendo que, eles de-
    vem estar postos em ordem crescente.
    
    list, int -> list
    """
    
    lista_1 = [n]
    lista_2 = lista_numeros + lista_1
    list.sort(lista_2)
    
    m = list.index(lista_2,n)
    lista_3 = lista_2[m:]
    list.sort(lista_3)
    
    return lista_3