def conta_numero(numero,matriz):
    """ dado um numero e uma matriz, conta e retorna quantas vezes o numero aparece na matriz"""
    linha=0
    lista=[]
    indice=0
    for linha in range(len(matriz)):
        for coluna in matriz[linha]:
            if numero == coluna[indice]:
                list.append(numero, lista)
            indice= indice +1
        linha= linha + 1
    return len(lista)