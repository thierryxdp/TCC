def media_matriz(matriz):
    i=0
    c=0
    soma=[]
    while i<len(matriz):
        soma=soma+[sum(matriz[i])]
        i=i+1
        while c<len(matriz[0]):
        	c=c+1
    return raund(sum(soma)/(i*c),2)