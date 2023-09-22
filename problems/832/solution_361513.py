def multmatriz(matriz, numero):
    """Multiplica uma dada matriz inteira por
    um dado número e retorna a matriz resultante.
       Entrada: list(list), int
       Saída: list(list)
    """
    resposta = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[0])):
            list.append(linha, matriz[i][j]*numero)
        list.append(resposta, linha)
    return resposta