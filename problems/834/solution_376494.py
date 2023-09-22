def media_matriz(matriz):
    '''Retorna a média de todos os números da
       matriz de entrada, com duas casas decimais;
       matriz->float'''
    i=0
    c=0
    while c<len(matriz):
        for e in matriz:
            soma=sum(matriz[i])
            t=len(matriz[i])
            r=soma/t
        i+=1
        c+=1
    return round(r,2)