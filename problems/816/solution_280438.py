def maiores(lista,n):
    """função que retorna todos os n ́umeros da lista original maiores que n
    list,int -> list"""
    if n not in lista:
        lista.append(n)
        lista.sort()
        i = lista.index(n)
        return lista[i+1:]