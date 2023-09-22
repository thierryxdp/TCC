def maiores(lista, n):
    '''
        Função que retorna uma lista que contém todos os números da lista original maiores que n.
        list(int) => list
    '''
    lista_maiores = []
    for i in lista:
        if(i > n):
            lista_maiores.append(i)
    lista_maiores.sort()
    return lista_maiores