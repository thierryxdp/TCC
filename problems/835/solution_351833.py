def melhor_volta (matriz):
    
    ''' Função que, dada uma matriz 6x10 
        com os tempos de 6 corredores em cada
        uma das 10 voltas de kart, retorna
        uma tupla informando de quem foi a melhor
        volta, com qual tempo e em que volta '''

corredores = range(1,7)
top_tempos = []
top_voltas = []
        
        for l in range(len(matriz)):
            for c in range(len(matriz[l])):
                if matriz[l][c] == min(matriz[l]):
                    top_tempos.append(matriz[l][c])
                    top_voltas.append(matriz[l].index(matriz[l][c]) + 1)
                    
tempo_vencedor = min(top_tempos)
indice_vencedor = top_tempos.index(tempo_vencedor)
corredor_vencedor = corredores[indice_vencedor]
volta_vencedora = top_voltas[indice_vencedor]

return (corredor_vencedor, tempo_vencedor, volta_vencedora)