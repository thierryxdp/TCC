def conta_numero(numero, matriz):
    quantidade = 0
    for linha in matriz:
        for Aij in linha:
            if linha[Aij] == numero:
                quantidade = quantidade + 1
    return quantidade