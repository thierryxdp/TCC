def soma_h(N):
    '''soma_h recebe um numero inteiro e devolve outro numero
    determine quantos divisores o numero n possui 
    int --> float'''
    
    soma = 0
    
    for numero in range(1,N+1):
        soma=soma+1/numero
        
    return round(soma,2)