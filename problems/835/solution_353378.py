def melhor_volta(matriz):
    '''analisa e retorna a melhor volta, o tempo necessário e qual a volta
    	list->int,int,int'''
    
    menor=[]
    
    for i in range(matriz):
        for j in range(matriz[0]):
            
            menor=menor+[min(matriz[i])]
            volta=list.index(menor,min(menor))
            quem=list.index(menor,min(menor))
            
    return quem,menor,volta