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
    lista_3 = lista_2[m+1:]
    list.sort(lista_3)
    
    return lista_3


def acima_da_media(lista_notas):
    """ Essa função recebe uma lista com as notas dos alunos
    de uma determinada turma. Posto isso, essa lista retorna-
    rá uma lista ordenada com as notas que ficaram acima da 
    média.
    
    list -> list
    """
    
    media = sum(lista_notas)/len(lista_notas)
    lista_ordenada = maiores(lista_notas,m)
    
    return lista_ordenada