def maiores(lista, n):
    '''função que, dada uma lista e um numero inteiro (n), retorna outra lista com todos os numeros 
    da lista original maiores que n. list, int -> list'''
    if n not in lista:
        lista.append(n)
        lista.sort()
        l= lista.index(n)
        lista2= lista[l+1:]
        rep= lista2.count(n)
        return lista2[rep:]