def conta_numero(numero,matriz):
    '''funcao conta quanas vezes o numero aparece na matriz. int,list->int'''
    cont=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                cont+=1
    return cont