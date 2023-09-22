def conta_numero(numero,matriz):
    '''função que dado um número retorna uma matriz de i'''
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