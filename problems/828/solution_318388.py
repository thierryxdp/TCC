def primo (i):
    '''Diz se um número inteiro é primo ou não, int->bool'''
    divisores = 0
    for elemento in range(100):
        if i%(elemento + 2)==0 and i!=(elemento+2):
            divisores = divisores + 1
    if divisores==0:
        return True
    else:
        return False