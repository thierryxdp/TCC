def media_matriz(matriz):
    '''Retorna a média de todos os números da
       matriz de entrada, com duas casas decimais;
       matriz->float'''
    i=0
    t=len(matriz[i])*len(matriz)
    soma=0
    for i in range(0,len(matriz)):
        soma+=sum(matriz[i])
        resultado=soma/t
    i+=1    
    return round(resultado,2)