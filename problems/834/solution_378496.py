def media_matriz(matriz):
    '''Entrada: Matriz -> dado do tipo list
       
       Saída: dado do tipo floar o qual representa a média de todos
       		 os numeros da matriz'''
    
    h=[]
    i=0
    for x in matriz:
        for y in x:
            list.append(h,y)
    p=sum(h)
    return round(p/len(h),2)