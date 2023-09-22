def melhor_volta(matriz):
    """Função que retorna de quem foi a melhor volta, com qual tempo e em 
    que volta. list -> tuple"""
    
    tempodecadaum = []
    for i in range(len(matriz)):
        menor_tempo = [min(matriz[i])]
        tempodecadaum = tempodecadaum + menor_tempo
    tempo = min(tempodecadaum)
    ganhador = list.index(tempodecadaum,tempo) + 1
    volta = list.index(matriz[ganhador-1],tempo) + 1
    
    return (ganhador,tempo,volta)