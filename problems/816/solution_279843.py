def maiores(lista,n):
    '''funcao que retirna uma lista que contenha
    todos os numeros da lista original maiores q N
    list->list'''
    if n not in lista:
        lista.append(n)
    lista.sort()
    l=lista.index(n)
    return lista[l+1:]