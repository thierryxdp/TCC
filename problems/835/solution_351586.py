def melhor_volta(matriz):
    menor = matriz[0][0]
    for i in range(len(matriz)):
        nums = matriz[i]
        for n in nums:
            if menor > n:
            menor = n
    return menor