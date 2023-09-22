def melhor_volta(matriz):
    nvoltas = len(matriz)
    ntempos = len(matriz[0])
    i = 0
    menor = []
    while i < nvoltas:
        menor = menor + min(matriz[i])
        i = i + 1
    valor = min(menor)
    volta = min.index(valor)
    a = matriz[volta-1]
    qual = a.index(valor)
    return (qual, valor, volta)