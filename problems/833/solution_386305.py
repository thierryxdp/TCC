def conta_numero(numero,matriz):
    ''' '''
    if matriz==[]:
        return 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            i+=1
       			return matriz[i].count(numero)