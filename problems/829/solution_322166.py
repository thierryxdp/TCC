def soma_h (n):
    '''
    	essa função calcular o valor de h baseado em n termos 
        h = 1 + 1/2 + 1/3 + ... +1/n
        int-> num
    ''' 
    x = 0
    for i in range(1, n+1):
        x = x + 1/i