def conta_numero(numero,matriz):
    """ Conta repeticoes de numero na matriz """
    soma = 0
    media = 0
    numElementos = len(matriz) * len(matriz[0])
    linha = 0
    while (linha < len(matriz)):
        for i in matriz[linha]:
            soma += i
        linha += 1
    media = soma / numElementos
    return media