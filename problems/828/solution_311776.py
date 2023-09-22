def primo (n):
    ''' função que retorna 'True' caso o número fornecido seja
        classificado como primo e 'False', caso contrário
        [int-->bool]'''
    
    if n == 2 or n == 1 :
        return True

    if n != 2 and n % 2 == 0 :
        return False
    
    else:
        
        divisores = 0 
        for inteiro in range(1,n+1):
            if n % inteiro == 0 :
                divisores += 1

        if divisores > 2:
            return False
        else :
            return True