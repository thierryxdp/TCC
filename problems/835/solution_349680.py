def melhor_volta(matriz):
    """recebe uma matriz 6x10 com os tempos em segundos dos 6 corredores em 
    cada uma das 10 voltas da corrida, e retorna uma tupla contendo  o numero,
    de 1 a 6, de quem teve a melhor volta, qual foi seu tempo, em segundos,
    e o numero, de 1 a 10 da volta na qual ele conseguiu isso
    list -> tuple"""
    
    linha = len(matriz)
    
    minimos = []
    
    for i in range(linha):
        menor = [min(matriz[i])]
        list.append(minimos, menor)
        
    menor_total = min(minimos)
    
    corredor = list.index(minimos, menor_total)
    
    volta = min(matriz[corredor])
    volta = list.index(matriz[corredor], volta)
    
    return (corredor + 1, menor_total[0], volta + 1)