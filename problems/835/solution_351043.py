def melhor_volta(matriz):
    '''retorna uma tupla informando de quem foi a melhor volta, o seu tempo e em qual volta'''
    '''list -> tuple'''
    
    melhores_voltas=[]
    melhor_volta=()
    i=0
    
    for i in range(6):
        for j in range(10):
            minimos=min(matriz[i])
            list.extend(melhores_voltas,[minimos])
            i=i+1   
         
    minimo=min(melhores_voltas)
    
    return (minimo)