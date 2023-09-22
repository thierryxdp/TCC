def conta_numero(numero,matriz):
    """ dado um numero e uma matriz, conta e retorna quantas vezes o numero aparece na matriz"""
    linha=0
    lista=[]
    coluna=0
    for linha in range(len(matriz)):
        if numero == matriz[linha]:
            list.append(numero, lista)
        linha= linha + 1
    return len(lista)