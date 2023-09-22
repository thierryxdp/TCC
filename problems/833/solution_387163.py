def conta_numero(numero,matriz):
    '''retorna o numero de vezes que o numero de entrada aparece
    na matriz
    int,list->int'''
    contador=0
    for i in matriz:
        for j in i:
            if j==numero:
                contador+=1
    return contador