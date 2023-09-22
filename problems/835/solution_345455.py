def melhor_volta(matriz):
    '''retorna quem fez a melhor volta da prova, o tempo e a volta'''
    menor=matriz[0][0]
    auxi=0
    auxj=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if menor>matriz[i][j]:
                menor=matriz[i][j]
                auxi=i
                auxj=j
    tupla=(menor,auxi,auxj)
    return tupla