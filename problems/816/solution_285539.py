def maiores(lista,n):
    '''Função que retorna uma lista com números maiores
    que o número inteiro n.
    obs: a lista de entrada também é de números inteiros
    valores: list, int --> list'''
    lista.append(n)
    lista.sort()
    return lista[lista.index(n)+1:]