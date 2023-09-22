def conta_numero(numero,matriz):
    ''' funcao que dado um numero inteiro e uma matriz de inteiro, conta e retorna quantas vezes aquele numero aparece'''
    i=0
    j=0
    resultado=0
    while i<len(matriz):
        while j<len(matriz[0]):
            if numero==matriz[i][j]:
                resultado+=1
    	    j=j+1
        i=i+1
        j=0
    return resultado