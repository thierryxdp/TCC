def fatorial(numero):
    '''calcula e retorna o fatorial do 
    num inserido
    float -> float'''
    copia_num = numero
    
    i = 1

    
    while i < copia_num:
        numero = numero*(copia_num-i)
        
        i = i + 1
        
    return numero