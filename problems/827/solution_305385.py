import math
def qtd_divisores(n) :
    num = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
            if (n / i == i) :
                num = num + 1
            else :
                num = num + 2

    return num