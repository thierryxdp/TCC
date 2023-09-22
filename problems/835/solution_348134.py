def melhor_volta(matriz):
    """ função que recebe uma matriz 6x10 de entrada, que corresponde a seis corredores, com seus tempos nas 10 voltas e retorna quem foi o melhor corredor, com o melhor tempo, na melhor volta
        entrada: lista
        saida: tupla
    """
    contador_piloto = 1
    contador_volta = 1 
    menor = matriz [0][0]
    
    for linha in range(len(matriz)): 
        for coluna in range(len(matriz[0])):
            if matriz[linha][coluna] < menor:
                menor = matriz[linha][coluna]
                contador_piloto = linha+1
                contador_volta = coluna+1
    return contador_piloto, menor, contador_volta