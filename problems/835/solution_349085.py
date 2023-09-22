def melhor_volta(matriz):
    ''' Dado uma matriz 6x10 com os tempos em segundos dos
    	corredores em cada volta, retorna uma tupla informando
        de quem foi a melhor volta da prova, com qual tempo e
        em que volta
        list -> tuple
     '''
    tupla = ()
    lista = []
    for i in matriz:
        for j in i:
            lista.append(j)
    lista.sort()
    melhor_tempo = lista[-1]
    for i in range(6):
        if melhor_tempo in matriz[i]:
            corredor = (matriz[i].index(melhor_tempo)) + 1
            volta = i + 1
    tupla += (corredor,)
    tupla += (melhor_tempo,)
    tupla += (volta,)
    return tupla