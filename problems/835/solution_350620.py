def melhor_volta(m):
    """ Recebe uma matriz "m" de entrada com o formato 6x10
    contendo o tempo dos 6 corredores em cada uma das 10 voltas
    e retorna uma tupla contendo o vencedor, o tempo do vencedor
    e volta """
    """ list -> tuple """
    Ganhador = Tempo = Volta = 9999
    for L in range(0,len(m)):
        for C in range(0,len(m[L])):
            if min(m[L][C], Tempo) == m[L][C]:
                Tempo = min(m[L][C],Tempo)
                Ganhador = L+1
                Volta = C+1
    return (Ganhador,Tempo,Volta)
#Caso de teste:
"""melhor_volta([[10,10,10,20,20,30,30,4,5,2],[2,2,3,3,3,4,5,6,3,5],[3,3,4,5,6,7,9,10,2,3],[4,3,4,7,8,7,9,10,2,3],[5,3,4,5,6,7,9,10,5,2],[6,3,4,5,6,7,9,10,2,10]])
>>> (6,2,9) """