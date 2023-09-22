def filtra_pares(tupla):
    """retorna os elementos pares. int -> int"""
    filtra = []
    for i in tupla:
        if i%2 == 0:
            filtra.append(tupla[i])