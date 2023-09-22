def primo (i):
    '''Diz se um número inteiro é primo ou não, int->bool'''
    divisor = 0
    while divisor==0:
        for elemento in range(i-1):
            if i%(elemento+1)==0:
                divisor = 1
    if divisor==0:
        return True
    else:
        return False