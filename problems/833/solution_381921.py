def conta_numero (numero,matriz):
    '''Retorna a quantas vezes o número informado aparece na matrix
    int, matrix->int'''
    linha=0
    col=0
    qtd=0
    for linha in len(matriz):
        for col in len(matriz[0]):
            if numero==matriz[linha][col]:
                qtd+=1
    return qtd