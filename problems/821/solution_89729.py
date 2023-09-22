def fatorial (n):
    '''calcula e retorna o fatorial de n'''
    '''int'''
    
    i = 1
    resultado = 1
    
    while i <= n:
        resultado = resultado * i
        
        i += 1
       
    return resultado