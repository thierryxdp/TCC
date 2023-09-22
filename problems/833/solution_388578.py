def conta_numero(numero,matriz):
    '''Conta na matriz informada quantas vezes o numero aparece. int, matriz -> int'''
    contador = 0
    for linha in matriz:
        for coluna in linha:
            if numero == coluna:
                contador += 1
    return contador

def conta_numero(numero,matriz):
    '''''''
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                contador += 1
    return contador

def conta_numero(numero,matriz):
    '''''''
    contador = 0
    for linha in matriz:
        qtd = linha.count(numero)
        contador += qtd
    return contador

def conta_numero(numero,matriz):
    '''''''
    lista = []
    for linha in matriz:
        for coluna in linha:
            lista.append(coluna)
    return lista.count(numero)