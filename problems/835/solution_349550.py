def melhor_volta (matriz):
    ''' Dado uma matriz 6x10 onde cada linha corresponde a um corredor
    e casa coluna a volta que foi dada na corrida, retorna qual corredor
    teve a melhor volta da prova, em qual tempo e em que volta;
    list -> tuple'''
    corredor = []
    menor_t = matriz [0][0]
    volta= 0
    for linha in matriz:
        qvolta = 0
        for tempo in linha:
            qvolta += 1
            if tempo < menor_t:
                menor_t = tempo
                volta= qvolta
                corredor= linha
    return ((list.index(matriz,corredor)+1),menor_t,volta)