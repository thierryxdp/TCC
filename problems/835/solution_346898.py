def melhor_volta(matriz):
    """Dada uma matriz 6x10 com os tempos em segundos de cada volta dos corredores
       retorna uma tupla dizendo de quem foi a melhor volta, seu tempo e em qual volta isto ocorreu.
       list[list] -> tupla"""
    
    if min(matriz[0]) < min(matriz[1]) and min(matriz[0]) < min(matriz[2]) and min(matriz[0]) < min(matriz[3]) and min(matriz[0]) < min(matriz[4]) and min(matriz[0]) < min(matriz[5]):
        melhorTempo = min(matriz[0])
        corredor = list.index(matriz, melhorTempo) + 1
        numeroVolta = list.index(matriz[0], melhorTempo) + 1
        
        return corredor, melhorVolta, numeroVolta
    
    elif min(matriz[1]) < min(matriz[0]) and min(matriz[1]) < min(matriz[2]) and min(matriz[1]) < min(matriz[3]) and min(matriz[1]) < min(matriz[4]) and min(matriz[1]) < min(matriz[5]):
        melhorTempo = min(matriz[1])
        corredor = list.index(matriz, melhorTempo) + 1
        numeroVolta = list.index(matriz[1], melhorTempo) + 1
        
        return corredor, melhorVolta, numeroVolta
    
    elif min(matriz[2]) < min(matriz[0]) and min(matriz[2]) < min(matriz[1]) and min(matriz[2]) < min(matriz[3]) and min(matriz[2]) < min(matriz[4]) and min(matriz[2]) < min(matriz[5]):
        melhorTempo = min(matriz[2])
        corredor = list.index(matriz, melhorTempo) + 1
        numeroVolta = list.index(matriz[2], melhorTempo) + 1
        
        return corredor, melhorVolta, numeroVolta
    
    elif min(matriz[3]) < min(matriz[0]) and min(matriz[3]) < min(matriz[2]) and min(matriz[3]) < min(matriz[1]) and min(matriz[3]) < min(matriz[4]) and min(matriz[3]) < min(matriz[5]):
        melhorTempo = min(matriz[3])
        corredor = list.index(matriz, melhorTempo) + 1
        numeroVolta = list.index(matriz[3], melhorTempo) + 1
        
        return corredor, melhorVolta, numeroVolta
    
    elif min(matriz[4]) < min(matriz[0]) and min(matriz[4]) < min(matriz[2]) and min(matriz[4]) < min(matriz[3]) and min(matriz[4]) < min(matriz[1]) and min(matriz[4]) < min(matriz[5]):
        melhorTempo = min(matriz[4])
        corredor = list.index(matriz, melhorTempo) + 1
        numeroVolta = list.index(matriz[4], melhorTempo) + 1
        
        return corredor, melhorVolta, numeroVolta
    
    elif min(matriz[5]) < min(matriz[0]) and min(matriz[5]) < min(matriz[2]) and min(matriz[5]) < min(matriz[3]) and min(matriz[5]) < min(matriz[4]) and min(matriz[5]) < min(matriz[1]):
        melhorTempo = min(matriz[5])
        corredor = list.index(matriz, melhorTempo) + 1
        numeroVolta = list.index(matriz[5], melhorTempo) + 1
        
        return corredor, melhorVolta, numeroVolta