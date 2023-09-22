def conta_numero(numero,matriz):
    """ Conta repeticoes de numero na matriz """
    ocorrencia = 0
    numLinhas = 0
    while (numLinhas < len(matriz)):
        for i in matriz[numLinhas]:
            if i == numero:
                ocorrencia += 1
        numLinhas += 1
    return ocorrencia