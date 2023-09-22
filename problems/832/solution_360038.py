def eh_quadrada(matriz):
    '''
    funcao criada para definir se uma matriz e quadrada ou nao
    parametros:
    matriz: matriz de qualquer tamanho
    saida:
    se e quadrada ou nao
    '''
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if len(matriz) == len(matriz[i]) and len(matriz[j]):
                return True 
            else:
                return False
            
            return True