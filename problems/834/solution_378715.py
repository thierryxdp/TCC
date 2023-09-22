def media_matriz(matriz): 
    '''funçao que retorna a media da matriz de entrada''' 
    '''list[list]->float'''
    lista=[]
    for i in range(len(matriz)):
        j=sum(matriz[i]) 
        p=len(matriz[i]) 
        r=(j/p)
        list.append(lista,r) 
    jj=len(lista) 
    pp=sum(lista)
    rr= round(pp/jj,2)
    return rr