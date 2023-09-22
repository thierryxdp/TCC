def maiores(listaNumeros, n):
    """função que dada uma lista e um numero'n', retorne outra lista com os valores da lista original maiores que 'n'"""
    if n not in lista:
        listaNumeros.append(n)
        listaNumeros.sort()
        i = listaNumeros.index(n)
        sublista = listaNumeros[i+1:]
        rep = sublista.count(n)
        return sublista[rep:]