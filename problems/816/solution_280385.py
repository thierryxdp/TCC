def maiores(lista,n):
    '''função que recebe uma lista e um numero int(n) e retorna
    uma nova lista com os numeros da lista original que
    são maiores que (n).
    list,int->List'''
    if n not in lista:
        lista.append(n)
        lista.sort()
        l = lista.index(n)
        lista2 = lista[l+1:]
        rep = lista2.count(n)
        return lista2[rep:]