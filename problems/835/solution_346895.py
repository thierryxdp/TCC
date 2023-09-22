def melhor_volta(matriz):
    """Dada uma matriz 6x10 com os tempos em segundos de cada volta dos corredores
       retorna uma tupla dizendo de quem foi a melhor volta, seu tempo e em qual volta isto ocorreu.
       list[list] -> tupla"""
    
    melhorTempo = []
    
    for indice1 in range(len(matriz)):
        pivo = matriz[indice1]
        
        for indice2 in range(len(pivo)):
            melhorTempo += min(pivo)
            corredor = list.index(matriz,pivo) + 1
            volta = list.index(min(pivo))
            
    return min(melhorTempo), corredor, volta