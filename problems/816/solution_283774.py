def maiores(lista,n):
    ''' retorna outra lista que contenha todos os numeros da lista original maiores que n, list,int->list'''
    if n in lista:
        lista1=sorted(lista)
        return lista1[list.index(lista1,n):len(lista1)]
    elif n not in lista:
        lista2=list.insert(lista,-1,n)
        lista3=list.sort(lista2)
        return lista3[list.index(lista3,n):len(lista3)]