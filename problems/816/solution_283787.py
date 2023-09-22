def maiores(lista,n):
    ''' retorna outra lista que contenha todos os numeros da lista original maiores que n, list,int->list'''
    if n in lista:
        lista1=sorted(lista)
        return lista1[list.index(lista1,n):len(lista1)]
    elif n not in lista:
        list.insert(lista,1,n)
        lista2=sorted(lista)
        return lista2[list.index(lista2,n):len(lista2)]