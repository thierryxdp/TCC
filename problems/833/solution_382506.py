def conta_numero(numero,matriz):
    linha = len(matriz[0])
    coluna = len(matriz)
    x = 0
    for i in range(linha):
        if i == numero:
            x = x +1
           
    return x