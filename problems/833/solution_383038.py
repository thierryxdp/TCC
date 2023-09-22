def conta_numero(numero,matriz):
    '''Funcao que recebe um numero e uma
matriz,conta e retorna quantas vezes aquele numero
aparece na matriz'''
    contagem = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if matriz[linha][coluna] == numero:
                contagem += 1
    return contagem