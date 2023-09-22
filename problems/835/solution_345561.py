def melhor_volta(matriz):
    '''recebe e retorna o piloto, o tempo e a volta em que foi conquistado o menor tempo da bateria
    	list(list) -> tup'''
    
    menor_volta = float('inf')
    
    for corredor, voltas in enumerate(matriz):
        for numero_volta, tempo_volta in enumerate(voltas):
            
            if (tempo_volta < menor_volta):
                menor_volta = tempo_volta
                corredor_vencedor = (corredor + 1)
                volta_vencedora = (numero_volta + 1)
                
    
    return (corredor_vencedor, menor_volta, volta_vencedora)