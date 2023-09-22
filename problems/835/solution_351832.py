def melhor_volta (matriz):
    
    ''' Função que, dada uma matriz 6x10 
        com os tempos de 6 corredores em cada
        uma das 10 voltas de kart, retorna
        uma tupla informando de quem foi a melhor
        volta, com qual tempo e em que volta '''
    
    top_corredores = []
    top_tempos = []
    top_voltas = range(1,11)
    
    for l in range(len(matriz)):
        top_tempos.append(min(matriz[l]))
        
        for c in range(len(matriz[l])):
            if matriz[l][c] in top_tempos:
                top_corredores.append(matriz[l].index(matriz[l][c]) + 1)
    
    melhor_tempo = min(top_tempos)
    index = top_tempos.index(melhor_tempo)
    melhor_volta = top_voltas[index]
    melhor_corredor = top_corredores[index]
    
    return (melhor_corredor, melhor_tempo, melhor_volta)