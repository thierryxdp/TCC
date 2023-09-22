def conta_numero(numero, matriz):
    '''analisa quantas vezes um inteiro aparece na matriz
       int, list -> int'''
    
    aparicoes=0
    
    for i in matriz:
        for j in i:
            if j==numero:
                aparicoes+=1
    return aparicoes