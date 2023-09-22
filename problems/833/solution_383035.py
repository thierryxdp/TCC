def conta_numero(numero,matriz):
    '''Funcao que recebe um numero e uma
matriz,conta e retorna quantas vezes aquele numero
aparece na matriz'''
    contagem = 0
    for linha in range(len(matriz)):
        if numero in linha:
            contagem += 1
            for coluna in range(len(matriz[0])):
                if numero in coluna:
                    contagem += 1
    return contagem