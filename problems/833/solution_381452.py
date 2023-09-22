def conta_numero(matriz,num):
    ''' Função que conta e retorna quantas vezes um numero passado como parametro de entrada aparece na matriz de inteiros; list(list)-> int'''
    l1=[]
    for linha in matriz: 
        for aij in linha:
            if aij==num:
                list.append(l1,num)
    return len(l1)