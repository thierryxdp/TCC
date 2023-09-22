import math


def soma_h(n):
    '''calcula e retorna o valor de H com n termos, H está descrito no enunciado
    int -> int'''
    
    
    soma = 0
    
    for i in range(1,n+1):
        soma = soma + math.pow(i,-1)
        
    return round(soma,2)