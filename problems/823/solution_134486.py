def faltante(lista):
    tamLista = len(lista) + 1
    n = 1
    pecas = [n]
    total_observado = sum(lista)
    while n < tamLista:
        pecas += [(n+1),]
        n = n+1
    total_esperado = total_observado + n
    peca_falt = total_esperado - total_observado
    if lista[0] != 1:
        return 1
    else:
        return peca_falt