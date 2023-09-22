def conta_numero(numero,matriz):
    """ dado um numero e uma matriz, conta e retorna quantas vezes o numero aparece na matriz"""
    contador=0
    lista=[]
    indice=0
    for contador in len(matriz):
        for contador in len(matriz[indice]):
            if numero == matriz[indice]:
                list.append(numero, lista)
            indice= indice +1
        contador= contador + 1
    return len(lista)