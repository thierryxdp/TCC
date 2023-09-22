def melhor_volta(mat):
    '''Recebe uma matriz 6x10 (6 linhas e 10 colunas) e
    retorna uma tupla com quem fez a melhor volta, o seu
    tempo e a volta em que foi feito. Sabe-se que todos
    os corredores têm tempos diferentes.
    list -> tuple'''
    i = 0
    menor = mat[0][0]
    volta = 1
    while i < len(mat):
        for tempo in mat[i]:
            if tempo < menor:
                menor = tempo
        		volta = list.index(mat[i],tempo) + 1
                corredor = i + 1
    	i += 1
    return (corredor, menor, volta)