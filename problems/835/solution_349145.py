def melhor_volta(matriz):
    menor = matriz[0][0]
    for r in range(len(matriz)):
        nums = matriz[r]
        for n in nums:
            menor = n if menor > n else menor
    return tuple(menor)