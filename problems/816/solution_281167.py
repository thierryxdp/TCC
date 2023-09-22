def maiores(lista,n):
    '''Dada uma lista de numeros inteiros e um
    numero inteiro n, retorna outra lista, que contem
    todos os numeros da lista original maiores que n
    list,int->list'''
    lista.append(n)
    lista.sort()
  
    return lista(list.index(lista,n)::)