def melhor_volta(matriz):
    '''Recebe uma matriz com os tempos em segundos dos
    corredores em cada volta, retorna uma tupla informando 
    de quem foi a melhor volta, com qual tempo e em que 
    volta
    list -> tupla'''
    
    corredor=[]
    volta=[]
    
    for i in range(matriz):
        melhor_tempo=min(matriz[i])
        list.append(corredor, melhor_tempo)
        melhor_volta=list.index(matriz[i],melhor_tempo)
        list.append(volta, melhor_volta)
    
    top_tempo=min(corredor)
    melhor_corredor=list.index(corredor, top_tempo)
    top_volta=volta[melhor_corredor]
    
    return (melhor_corredor+1,top_tempo,top_volta+1)