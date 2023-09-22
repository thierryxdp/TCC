def melhor_volta(m):
    """função que retorna a melhor volta da prova, com qual tempo e em que volta,
    através da matriz de entrada m;
    Entrada: list
    Saída: tuple"""
    final = []
    resposta = ()
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            menortempo = min(matriz[i])
            list.append(final,menortempo)
            resultado = min(final)
            if matriz[i][j] == resultado:
                posicao = j + 1
                volta = i +1
        resposta = (volta, resultado, posicao)
    return resposta