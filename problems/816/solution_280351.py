def maiores(lista, n):
    """função que dada uma lista e um numero'n', retorne outra lista com os valores da lista original maiores que 'n'"""
    if n not in lista:
        lista.append(n)
        lista.sort()
        i = lista.index(n)
        sublista = lista[i+1:]
        rep = sublista.count(n)
        return sublista[rep:]