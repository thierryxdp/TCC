def faltante(lis):
    menor = min(lis)
    maior = max(lis)
    faltando = list()
    for c in range(menor, maior + 1):
        if c not in lis:
            faltando.append(c)
    return faltando