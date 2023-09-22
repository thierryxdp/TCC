def min(matriz):
    menor = matriz[0][0]
    for r in range(matriz):
        nums = matriz[r]
        for n in nums:
            menor = n if menor > n else menor
    return menor
def obter_indice_menor(lista):
    """Devolve o índice da menor nota"""
    indice_menor = 0
    menor_nota = lista[0]
    for i, nota in enumerate(lista):
        if nota < menor_nota:
            menor_nota = nota
            indice_menor = i
    return indice_menor
def melhor_volta(matriz):
    lista=[]
    tempo= min(matriz)
    corredor= obter_indice_menor(matriz)
    volta= matriz[corredor]
    #volta1=encontar_elemento(volta,tempo)
    volta1=volta.index(tempo)
    volta1=volta1+1
    corredor=corredor+1
    lista.append(corredor)
    lista.append(tempo)
    lista.append(volta1)
    return tuple(lista)