def min(matriz):
    menor = matriz[0][0]
    for r in range(len(matriz)):
        nums = matriz[r]
        for n in nums:
            menor = n if menor > n else menor
    return menor
def melhor_volta(matriz):
    lista=[]
    tempo= min(matriz)
    quem= lista.index[tempo]
    lista.append(quem)
    lista.append(tempo)
    return lista