def media_matriz(matriz):
    soma=0
    d=0
    for i in range(len(matriz)):
        for x in matriz[i]:
            soma=soma+x
        	d+=len(matriz[i])
   		media=soma/d   
    return round(media,2)