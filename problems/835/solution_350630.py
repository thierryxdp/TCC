def melhor_volta(matriz):
    """
    Essa função recebe uma matriz 6x10 com os tempos em segundos 
    dos competidores em cada volta e retorna uma tupla contendo de 
    quem foi a melhor volta, com qual tempo e em que volta;
    list -> tuple
    """
    minimo_corredores = []
    for i in matriz:
        minimo_corredores.append(min(i))
    minimo = min(minimo_corredores)
    vencedor = 1
    for listas in matriz:
        for j in range(1, 11):
            if minimo in listas:
                volta = j
    for listas in matriz:
        if minimo in listas:
            return (vencedor, minimo, volta)
        vencedor += 1