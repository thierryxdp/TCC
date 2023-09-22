def melhor_volta(matriz):
# A função recebe uma matriz 6x10 com os tempos em segundos dos corredores de cada volta e deve
# retornar uma tupla informando de quem foi a melhor volta, qual foi o tempo e em que volta foi
# registrado esse tempo. Todos os tempos registrados são diferentes.
# corredores numerados de 1 a 6 ; voltas numeradas de 1 a 10.
# list->tuple
    minimos=[]
    qual_volta=[]
    for i in range(len(matriz)):
        list.append(minimos,min(matriz[i]))
        list.append(qual_volta,list.index(matriz[i],minimos[i]))
    corredor=list.index(minimos,min(minimos))
    tempo=min(minimos)
    volta=qual_volta[corredor]
    return ((corredor+1,tempo,volta+1))