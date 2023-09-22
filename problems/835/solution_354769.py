def melhor_volta(m):
    menor_tempo=[]
    for indice in m:
        menor_tempo+=[min(indice)]
    corredor= list.index(menor_tempo,min(menor_tempo))+1
    for x in m:
        for voltas in x:
            if min(menor_tempo)==voltas:
                melhor_volta=list.index(x,min(menor_tempo))+1
    return (corredor,min(menor_tempo),melhor_volta)