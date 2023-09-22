def soma_h(n):
    '''Retorna o numero de somas n de uma série h
    int --> float'''
    resultado = 0
    i = 0
    for numero in range(n):
        i = i+1
        resultado = resultado + (1/i)
        
    return round(resultado,2)