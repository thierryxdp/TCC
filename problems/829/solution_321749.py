def soma_h(num):
    ''' Função que calcula e retorna o valor de H 
    int->float'''
    somatorio=0
    for i in range(1, num+1):
        
        somatorio = somatorio + (1/i)

    return somatorio