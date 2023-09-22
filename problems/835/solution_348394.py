def melhor_volta(matriz: list) -> tuple:
    """Receba como entrada uma matriz 6 × 10 com os tempos em segundos dos corredores
    em cada volta e retorna uma tupla informando de quem foi a melhor volta da prova,
    com qual tempo e em que volta"""
    
    lista = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(lista,matriz[i][j])
        melhor_tempo = min(lista)        
        if melhor_tempo in matriz[i]:
            melhor_corredor = i + 1
        for j in range(len(matriz[i])):
            if matriz[i][j] == melhor_tempo:
                numero_volta = j + 1
    return (melhor_corredor, melhor_tempo, numero_volta)