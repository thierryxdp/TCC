def soma_h(n):
    ''' Função que calcula e retorna o valor H com n termos da formula dada
    int->float'''
    
    somatorio=0
    
    for i in range(1, n+1):
        
        somatorio = somatorio + (1/i)

    return somatorio