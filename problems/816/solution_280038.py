def maiores (lista,n):
    '''Retorna uma lista contendo todos valores maiores que n presentes
    na lista original
    list,int-> lista'''
    if n in not lista:
    list.append(lista,n)
    crescente= list.sort(lista)
    posicao = list.index(lista,n)
    nova_lista = lista[posicao:]
    return nova_lista