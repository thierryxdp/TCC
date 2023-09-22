def faltante(lista):
    tamLista = len(lista) + 1
    n = 1
    pecas = [n]
    total_observado = sum(lista)
    while n < tamLista:
        pecas += [(n+1),]
        n = n+1
    total_esperado = total_observado + n
    peca_falt = total_observado - n
    if total_observado == n:
        return total_esperado - total_observado
    if total_observado != n:
        return peca_falt
    if lista[0] != 1:
        return 1