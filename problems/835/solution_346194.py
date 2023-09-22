def melhor_volta(matriz):
    """função que recebe uma matriz com os tempos dos corredores e retorna uma tupla informando de quem foi a melhor volta;
    list -> tupla"""
    acumulador = [ ]
    for i in matriz:
        for c in i:
            list.append(acumulador,c)
    pior = min(acumulador)
    index = acumulador.index(pior)
    tempo = acumulador[index]
    competidor = int((str(index)[0])) + 1
    if index<10:
        competidor = 1
        volta = int((str(index)[0])) + 1
    else:
        volta = int((str(index)[1])) + 1
    return competidor,tempo,volta