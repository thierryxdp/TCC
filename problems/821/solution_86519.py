def fatorial(n):
    '''Retorna o valor de n fatorial; int -> int'''
   	if n < 0: 
        return 0
    elif n == 0:
        return 1
    elif n == 1: 
        return 1
    else: 
        fatorial = 1
        while(n > 1): 
            fatorial *= n 
            n -= 1
        return fatorial