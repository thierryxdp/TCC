def mediah(matriz:List):
    soma = 0
    for linha in matriz:
        for aij in linha:
                soma += aij
    return soma/len(matriz)