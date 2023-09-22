def melhor_volta(matriz):
    '''Função que retorna a melhor volta, quem deu, e em quanto tempo
    list -> tuple'''
    podium = []
    esparro = []
    i = 0
    
    for hamilton in range(6):
        menorTempo = min(matriz[hamilton])
        volta = list.index(matriz[hamilton], menorTempo)
        list.append(podium, [(hamilton+1), menorTempo, (volta+1)]) 
        
    for h in range(6):
        list.append(esparro, podium[h][1])
        
    knot = min(esparro)
    slip = list.index(esparro, knot)
    
    return tuple(podium[slip])