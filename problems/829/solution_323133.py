def soma_h(n):
    soma = 0
    
    '''Por meio de while'''
    #i = 1
    #while i <= n:
        #soma += 1/i
        #i += 1
    #return round(soma, 2)
    
    '''Por meio de for'''
    for num in list(range(2,n+1)):
        soma += 1/num
    return round(soma, 2)