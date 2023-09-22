import math
def qtd_divisores(n) :
    '''Retorna quantos divisores um numero tem
    int-->int'''
    num = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
            if (n / i == i) :
                num = num + 1
            else :
                num = num + 2

    return num