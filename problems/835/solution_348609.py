def melhor_volta(matriz):
    """Retorna uma tupla informando de quem foi a melhor volta da prova, o seu tempo e em que volta.
    lista --> tupla"""
    
    tempo = []
    
    for i in range(len(matriz)):
        list.append(tempo,min(matriz[i]))
    
    index_quem = list.index(tempo,min(tempo))
    volta = list.index(matriz,min(matriz[index_quem]))
                    
    
    return (index_quem + 1, min(tempo), volta)