def media_matriz(matriz):
    '''retorna a media de todos os elementos de uma 
    matriz nao vazia, com duas casas decimais 
    de precisao; list -> float'''
    soma=0
    divisor=0
    j=0
    i=0
    while j<len(matriz):
        while i<len(matriz[j]):
            soma=soma+matriz[j][i]
            i=i+1
            
        j=j+1
        divisor=divisor+i
        i=0
    return round(soma/divisor,2)