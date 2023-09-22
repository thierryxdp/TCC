def maiores(lista,n):
    '''Caso um numero da lista seja maior que n, ele é adicionado na lista2 e a função retorna a lista2 ordenada
       list, int -> list'''
    lista2 = []
    for x in lista:
        if x > n:
            lista2.append(x)
    return sorted(lista2)