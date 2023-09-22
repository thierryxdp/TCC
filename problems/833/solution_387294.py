def conta_numero(numero, matriz):
    '''Função que dado um número e uma matriz, conta quantas vezes
    esse número aparece na raiz.
    numero -> int
    matriz -> list
    return -> int'''
    
    aparece = 0
    
    
    for i in range(len(matriz)):
        
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                aparece += 1
                       
    return aparece