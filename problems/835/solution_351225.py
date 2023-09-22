def melhor_volta(m):
    '''recebe uma matriz 6x10 com os tempos dos corredores
    de kart por volta e retorna de quem foi a melhor volta,
    com qual tempo e em que volta
    list(list)->tuple'''
    tempos = []
    voltas = []
    for i in range(len(m)):#corredores
        menor = min(m[i])
        list.append(tempos,menor)
        list.append(voltas,list.index(m[i],menor))
    #duas listas contendo os tempos e em que volta foi
    indice = list.index(tempos,min(tempos))
    return(indice + 1,min(tempos),voltas[indice]+1)