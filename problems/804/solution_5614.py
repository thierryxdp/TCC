def filtra_pares(tupla):
    posicoes = [t1,t2,t3,t4]
    for i, n in enumerate(tupla):
        if n % 2 == 0:
            posicoes.append(i)
    return posicoes