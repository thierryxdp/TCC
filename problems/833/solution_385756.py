def conta_numero(numero,matriz):
    contador = 0
    for linhas in matriz:
        for numeros in linhas:
            if numeros == numero:
                contador = contador + 1
    return contador