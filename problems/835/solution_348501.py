def melhor_volta(resultados):
    ''' função que informa de quem foi a melhor volta da prova, com qual tempo, e em que volta;
    list -> tuple '''
    melhor = []
    for i in resultados:
        list.append(melhor, min(i))
    b = min(melhor)
    a = list.index(melhor, b)
    c = list.index(resultados[a], b)
        return (a+1, b, c+1)