def conta_numero(numero: int, matriz: List):
    """funcao que recebe um numero inteiro e uma matriz de inteiros de tamanho qualquer,conta e retorna quantas vezes aquele numero aparece e retorna quantas vezes aquele numero aparece na matriz;int,list ->list"""
    conta = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                conta = conta + 1
    return conta