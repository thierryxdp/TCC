def maiores(lista,n):
    ''' retorna outra lista que contenha todos os numeros da lista original maiores que n, list,int->list'''
    if n in lista:
        lista1=sorted(lista)
        lista2=lista1[list.index(lista1,n):len(lista1)]
        return lista2