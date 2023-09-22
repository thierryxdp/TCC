def media_matriz(matriz):
    """Essa função retorna a media de todos os numeros de uma matriz"""
    """list->float"""
    i=0
    c=0
    soma=[]
    while i<len(matriz):
        soma=soma+[sum(matriz[i])]
        i=i+1
        while c<len(matriz[0]):
        	c=c+1
    return round(sum(soma)/(i*c),2)