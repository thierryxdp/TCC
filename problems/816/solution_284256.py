def maiores (lista: list, n: int) ->list:
    copialista = lista.copy()
    copialista.append(n)
    copialista.sort()
    posicao = copialista.index(n)
    maiores = copialista[posicao + 1:]
    if n in maiores:
        quant = maiores.count(n)
        maiores = maiores[quant:]
    return maiores