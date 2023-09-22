def melhor_volta(matriz):
    '''Função que recebe uma matriz 6X10 onde as linhas são os jogadores, as colunas
    são as voltas e os elementos são os tempos de cada volta. Retorna uma tupla com o
    jogador da melhor volta, o menor tempo e em qual volta teve o melhor tempo.
    Entrada: list. Saída: tuple'''
    menor=100
    for L in range(len(matriz)):
        for C in range(len(matriz[L])):
            if matriz[L][C]<menor:
                menor=matriz[L][C]
                linha=L
                coluna=C          
    return linha+1,menor,coluna+1