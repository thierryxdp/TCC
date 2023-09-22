def melhor_volta(matriz):
    """Retorna uma tupla informando: de quem foi a melhor volta da prova,
    com qual tempo e em que volta, dados: uma matriz(6x10) com os tempos
    em segundos dos corredores em cada volta."""
    
    
    menos = []
    for i in range(len(matriz)):
        menos.append(min(matriz[i]))
        menor = min(menos)
        
        if menor in matriz[i]:
            quem = matriz.index(matriz[i])+1
            qual = matriz[i].index(min(menos))+1
            
    return (quem, menor, qual)