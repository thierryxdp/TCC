def conta_numero(numero,matriz):
    '''analisa e retorna quantas vezes o número aparece na matriz
    	int,list->int'''
    
    qtd=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            
            if matriz[i][j]==numero:
                
                qtd=qtd+1
                
    return qtd