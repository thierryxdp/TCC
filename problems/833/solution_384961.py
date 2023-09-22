def conta_numero(numero, matriz):
    """Função que verifica quantas vezes o numero informado aparece na matriz.
    Parametros: int, lista->int"""
    quantidade = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                quantidade += 1
    return quantidade