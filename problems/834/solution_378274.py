def media_matriz(matriz):
    '''Função que retorna a média de todos os números da 
    matriz
    entrada=list
    saida=float'''
    h=[]
    i=0
    for x in matriz:
        for y in x:
            list.append(h,y)
    p=sum(h)
    return round(p/len(h),2)