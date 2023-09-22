def soma_h(N):
    '''calcula o valor de H com apenas 2 casas decimais
    int -> float'''
    
    a=1
    H=0
    
    while 1<=N:
        H+=1/a
    return round(N,2)