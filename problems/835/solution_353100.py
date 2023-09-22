def melhor_volta(m):
    """Essa função retorna de quem foi a melhor volta, o tempo e qual volta foi
    lista->tupla"""
    
    lista = min(m)
    
    corredor = list.index(m,lista)
    tempo = min(lista)
    volta = list.index(lista,tempo)
    
    return (corredor +1,tempo,volta+1)
    
    
    
    
                
    return (corredor,tempo,volta)