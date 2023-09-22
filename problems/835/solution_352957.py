def melhor_volta(matriz):
    menores_voltas=[]
    volta=0
    corredor=0
    menor_volta=0
    
    for i in range(6):
    	menores_voltas+=[min(matriz[i])]
        
    menor_volta=(min(menores_voltas))
    corredor=menores_voltas.index(min(menores_voltas))+1
    volta=matriz[corredor].index(menor_volta)+1
   
    return (corredor,menor_volta,volta)