def conta_numero(numero,matriz):
    '''
    funcao que conta um determinado numero presente em uma matriz
    parametros:
    numero--->int
    matriz--->list
    saida:
    int
    '''
    i=0
    lista=[]
    while i<len(matriz):
        if numero in matriz[i]:
            lista.append(matriz[i].count(numero))
        i+=1
    return sum(lista)