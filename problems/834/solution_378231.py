def soma(n):
    s=0
    for i in range(len(n)):
        s+= i
    return s
def media_matriz(matriz):
    return (list(map(soma, matriz))))