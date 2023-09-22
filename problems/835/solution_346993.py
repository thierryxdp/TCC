def melhor_volta(matriz_tempos):
#idéia: pegar a matriz 6x10,supor que o valor
#minimo esta na posição m[o][o],caso nao esteja,
#fazer o contador andar por toda matrizachando o
#menor, assim que achar o menor de todos ela vai
#substituir no valor minimo.'''
	tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempos[i][j] < tupla[1]:
                tupla = (i+1,matriz_tempos[i][j],j+1)
    return tupla