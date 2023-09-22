def melhor_volta(matriz):
    """Função que recebe o tempo de 6 corredores em cada uma das 10 voltas e retorna quem fez a melhor volta, 
    com qual tempo e em que volta"""
    lista = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(lista, matriz[i][j])
            
    tempo = min(lista)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == tempo:
                corredor = i
                volta = j
            
    return (corredor, tempo, volta)