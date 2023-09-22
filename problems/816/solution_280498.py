def maiores(listaNumeros, n):
    '''funçao que dada uma lista e um numero retorna outra lista contendo todos os numeros da lista original maior que n'''
    '''list, int -> list'''
    if n not in listaNumeros:
        listaNumeros.append(n)
        listaNumeros.sort()
        i = listaNumeros.index(n)
        sublista = listaNumeros[i+1:]
        rep = sublista.count(n)
        return sublista[rep:]