def soma(n):
    s=0
    for i in range(len(n)):
        s+= n[i]
    return s
def media_matriz(matriz):
    return round(sum(map(soma, matriz)) / (len(matriz) * len(matriz[0])),2)