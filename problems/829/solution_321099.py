def soma_h(n):
    '''Calcula e retorna o valor da equação H com n termos,
    onde n e inteiro e dado como entrada.
    int -> int/float'''
    
    soma=0
    
    for numero in range(1,n+1):
        soma+=1/numero
        
    return round(soma,2)