def melhor_volta(matriz):
    '''Retorna o corredor do menor tempo de volta, o tempo da volta e o numero da volta'''
    #list -> tuple
    menores_tempos = []
    for linha in matriz:
        for Aij in linha:
            if Aij == min(linha):
                list.append(melhores_tempos, Aij)
    corredor = 1
    for tempo in menores_tempos:
        corredor = corredor + 1
        if tempo == min(menores_tempos):
        	menor_tempo = tempo
    return (corredor, menor_tempo)