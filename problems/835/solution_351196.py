def melhor_volta(matriz):
    '''retorna uma tupla informando de quem foi a melhor volta, o seu tempo e em qual volta'''
    '''list -> tuple'''
    
    melhores_voltas=[]
    i=0
    
    for i in range(6):
        minimos=min(matriz[i])
        for j in range(10):
            list.extend(melhores_voltas,[minimos])
            i=i+1
    minimo=min(melhores_voltas)
    
    for i in range(10):
        if minimo in matriz:
            volta=list.index(matriz[i],minimo)
            i=i+1
            
    tupla=(minimo,volta+1)
    
    return tupla