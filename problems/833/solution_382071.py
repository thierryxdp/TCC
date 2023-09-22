def conta_numero(numero,matriz):
    """ dado um numero e uma matriz, conta e retorna quantas vezes o numero aparece na matriz"""
    linha=0
    lista=[]
    coluna=0
    for linha in range(len(matriz)):
        for coluna in linha:
            if numero == matriz[coluna]:
                list.append(numero, lista)
            coluna= coluna +1
        linha= linha + 1
    return list.count(numero,lista)