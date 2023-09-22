def conta_numero(numero,matriz):
    '''retorna a ocorrencia de um numero na matriz
    int,list->int'''
    
    numeros=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero+= j
   	
    return list.count(numeros,numero)