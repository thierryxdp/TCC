def maiores(listanum, n):
    """funcao que dada uma lista e um numero inteiro, retorna outra lista com todos os numeros da lista original maiores que n"""
    """list -> list"""
    if n not in listanum:
        listanum.append(n)
        listanum.sort()
        i = listanum.index(n)
        sublista = listanum[i+1:]
        rep = sublista.count(n)
        return sublista[rep:]