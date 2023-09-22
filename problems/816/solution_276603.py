def maiores(lista,n):
    '''Dada uma lista de numeros inteiros e um inteiro 'n';
    retorna outra lista com os números da lista original maiores que 'n';
    list, int => list'''
    if lista[1]<int(n):
        list.remove(lista,lista[1])
        return lista
    elif lista[2]<int(n):
        list.remove(lista,lista[2])
        return lista
    elif lista[3]<int(n):
        list.remove(lista,lista[3])
        return lista