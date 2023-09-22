def melhor_volta(m):
    """funcao que dada uma matriz 6x6 com os tempos das 10 voltas dos
       6 pilotos inseridos calcula e retorna uma tupla contendo
       o numero da volta de menor tempo, o tempo e o piloto que a fez

       lista-> tupla
    """

    tempos=[]

    for i in range(6):
        for j in range(10):
            tempos= tempos+m[i][j]

    menor_tempo= min(tempos)

    for i in range(10):
        for j in range(6)
        if menor_tempo in m[j]:
        return (j , menor_tempo, i)