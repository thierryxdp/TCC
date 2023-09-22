def maiores(lista_num, n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna
outra lista, que contenha todos os números da lista original maiores que n
    list, int -> list
    '''
    list.append(lista_num,n)
    list.sort(lista_num)
    pos = list.index(lista_num,n)
    del lista_num[:pos]
    list.remove(lista_num,n)
    if list.count(lista_num,n) != 0:
        idc = list.count(lista_num,n)
        lista_num = lista_num[idc:]
    return lista_num