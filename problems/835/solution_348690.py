def melhor_volta(x):
    '''Dada uma matriz 6x10 com os tempos, em segundos, dos corredores em cada volta, retorna de quem foi a melhor volta, com qual tempo e em qual volta.
    list -> tuple'''
    melhor_de_cada_j=[]
    for j in range (6):           
        list.append(melhor_de_cada_j,(min(x[j])))
        #Coloca em uma lista o melhor tempo de cada jogador.
    #Terá o tempo gasto.
    v=min(melhor_de_cada_j)
    v=melhor_de_cada_j.index(v)
    return (v+1,min(melhor_de_cada_j),v+1)