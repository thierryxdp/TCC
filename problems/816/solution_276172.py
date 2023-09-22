def maiores(lista,n):
    '''Dada uma lista de numeros inteiros e o numero inteiro n, essa função retorna outra lista
    que contem todos os numeros maiores que n da lista original
    list,int-->list'''
    lista1=lista[:]
    list.append(lista1,n+0.5)
    list.sort(lista1)
    lista1=lista1[list.index(lista1,n)+1:]
    return lista1