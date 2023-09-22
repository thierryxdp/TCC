def melhor_volta(matriz):
    '''retorna qual piloto teve a menor volta, qual foi
    seu tempo e em que volta foi dada
    matriz->tuple'''
    menores_voltas=[]
    volta=0
    corredor=0
    menor_volta=0
    
    for i in range(6):
    	menores_voltas+=[min(matriz[i])]
        
    menor_volta=(min(menores_voltas))
    corredor=menores_voltas.index(min(menores_voltas))
    volta=matriz[corredor].index(menor_volta)
    corredor, volta = corredor+1, volta+1
    
    return (corredor,menor_volta,volta)