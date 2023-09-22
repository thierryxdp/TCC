def melhor_volta(mat):
    '''Recebe uma matriz 6x10 (6 linhas e 10 colunas) e
    retorna uma tupla com quem fez a melhor volta, o seu
    tempo e a volta em que foi feito. Sabe-se que todos
    os corredores têm tempos diferentes.
    list -> tuple'''
    corredor = 1
    menor = mat[0][0]
    volta = 1
    while (corredor - 1) < len(mat):
        for tempo in corredor:
            if tempo < menor:
                menor = tempo
        		volta = list.index(corredor,tempo) + 1
    corredor += 1
    return (corredor, menor, volta)