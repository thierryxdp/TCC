def conta_numero(numero,matriz):
    """Função que dada uma matriz e um número, verifica o número de ocorrências desse número na matriz. int , list -> int"""
    contador = 0
    for n in range(len(matriz)):
        for m in range(len(matriz[n])):
            if matriz[n][m] == numero:
                contador += 1
    return contador