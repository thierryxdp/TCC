def media_matriz(matriz):
    ''' Função que recebe uma matriz e soma os seus valores e 
    	retorna a média.
        list(list)--->>float'''
    n=0
    r=[]
    for i in range(len(matriz)):
        x=0
        for j in range(len(matriz[-1])):
            if i or j in range(0,11):
                n=n+1
            x+= matriz[i][j]
        list.append(r,x)
    
    return round(sum(r)/n,2)