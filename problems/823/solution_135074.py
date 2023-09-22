def faltante(lista):
    
    list.sort(lista)

    cont = 0
        
    
    
    while len(lista) > cont:
        if len(lista) <= 2:
            
            x = (lista[cont] + lista[cont + 1]) // 2
        
            if x != lista[cont] and x < lista[cont+1]:
                return x
            else: 
                cont += 1
                
        else: 
            x = (lista[cont-1] + lista[cont + 1]) // 2
        
            if x > lista[cont-1] and x < lista[cont+1]:
                return cont
            else: 
                cont += 1