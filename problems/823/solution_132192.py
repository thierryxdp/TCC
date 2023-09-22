def faltante(lista):
    
    Q = len(lista)
    i = 0
    
    while i < Q-1:
        if Q == 1 and lista[0] == 1:
            return lista[0] + 1
        
        elif lista[0] != 1:
            return lista[0] - 1
        
        elif Q > 1:
            if lista[i] != lista[i+1] - 1:
                return lista[i + 1] - 1
            
            i = i + 1
            
    return lista[-1] + 1