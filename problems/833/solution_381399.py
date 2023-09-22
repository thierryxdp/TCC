def conta_numero(numero,matriz):
    '''conta_numero recebe um numero inteiro e uma matriz e
    devolve um numero inteiro
    determine  quantidade de vezes que esse numero se encontra na matriz
    int, list(list) --> int'''
    
    resposta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[j])):
            if matriz[i][j]==numero:
                list.append(resposta,matriz[i][j])                             
        
    return len(resposta)