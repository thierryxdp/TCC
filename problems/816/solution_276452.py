def maiores(lista, n):
    '''função que dada uma lista de números inteiros e um número inteiro n retorna outra lista, composta pelos números
    da lista maiores que n.
    list, int -> list'''
    
    list.append(lista, n)
    list.sort(lista)
    posicao = list.index(lista, n)
    
    
    return lista[posicao+1:]