def melhor_volta(m):
    """Essa função retorna de quem foi a melhor volta, o tempo e qual volta foi
    lista->tupla"""
    
    corredor = 0
    tempo = 0
    volta = 0
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j-1]> m[i][j]:
                corredor = i+1
                tempo = m[i][j]
                volta = j+1
                
    return (corredor,tempo,volta)