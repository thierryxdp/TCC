def melhor_volta(matriz):
    """função de kart que rcebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores 
    em cada volta. a função deve retornar uma tupla informando: de quem foi a melhor volta da prova, com qual tempo
    e em que volta. Assuma que os corredores tem tempos diferentes
    list(list) -> tuple(int,int,int)"""
    
    melhores_voltas = []
    for i in range(len(matriz)):
        melhores_voltas.append(min(matriz[i]))
    melhor_volta = min(melhores_voltas)
    quem_foi = list.index(melhores_voltas,melhor_volta) + 1
    num_volta = list.index(matriz[quem_foi -1],melhor_volta) + 1
    return(quem_foi,melhor_volta,num_volta)