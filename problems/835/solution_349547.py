def melhor_volta (matriz):
    ''' Dado uma matriz 6x10 onde cada linha corresponde a um corredor
    e casa coluna a volta que foi dada na corrida, retorna qual corredor
    teve a melhor volta da prova, em qual tempo e em que volta;
    list -> tuple'''
    corredor = 1
    volta = 0
    menor_t = 0
    for linha in matriz:
        for tempo in linha:
            volta += 1
            if tempo < menor_t:
                menor_t = tempo
                corredor = linha
                
    return (corredor,menor_t,volta)