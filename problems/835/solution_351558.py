def melhor_volta(matriz):
    '''retorna uma tupla informando de quem foi a melhor volta, o seu tempo e em qual volta'''
    '''list -> tuple'''
    
    melhores_voltas=[]
    
    
    for i in range(6):
        minimos=min(matriz[i])
        for j in range(10):
            list.extend(melhores_voltas,[minimos])
            i=i+1
           
    minimo=min(melhores_voltas)
    
    
    
    for i in range(6):
        for j in range(10):
            if minimo == matriz[i][j]:
                tupla=(i+1, minimo, j+1)
    
    return tupla