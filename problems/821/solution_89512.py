def fatorial(n):
    
    '''Função que dado um número inteiro, calcula e retorna seu fatorial. int -> int'''
    
    i = 1
    valor = 1
    
    while i < n:
        valor = valor*(i + 1)
        i = i + 1
        
    return valor