def primo(n):
    '''Esta função verifica se umm número n é primo ou
não. Se sim, retorna True; caso contrário, False.
int --> bool
'''
    quant_divis = 0
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(1,n+1):
            if (n % i) == 0:
                quant_divis += 1
            if quant_divis > 3:
                return False
    return True