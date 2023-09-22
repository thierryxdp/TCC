def melhor_volta(matriz):
    '''retorna uma tupla informando de quem foi a melhor volta, o seu tempo e em qual volta'''
    '''list -> tuple'''
    
    minimos=[]
    
    for i in range(6):
        for j in range(10):
            elem=min(matriz[i])
            list.extend(minimos, elem)
    minimo=min(minimos)
    elem=list.index(matriz, minimo)
    
    return (minimo,elem)