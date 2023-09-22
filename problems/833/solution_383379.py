def conta_numero(numero,matriz):
    """Funcao que irá retornar quantas vezes o numero irá aparecer na matriz
    Sendo número dado pela variável número. 
    Entrada: lista | Saída: Int """
    contador = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                contador += 1
    return contador