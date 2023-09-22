import math
def qtd_divisores(num):
    result = 1 + num
    for i in range(2, int(math.sqrt(num)) + 1):
        d, r = divmod(num, i)
        if r == 0: 
            result += i; 
            if i != d: 
                result += d; 
            return result