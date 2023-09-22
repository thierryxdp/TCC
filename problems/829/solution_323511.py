def soma_h(N):
    '''função que calcula a somatória de frações com N numero
    de termos, dado o numero N a ser somado.
    N -> int
    return -> float'''
    
    somatorio = 0
    
    for num in range(N+1):
        somatorio += N**-1
        
    return round(somatorio, 2)