import math

def qtd_divisores(num):
    """Soma os divisores de um determinado num; int=>int"""
    resultado = 1 + num
    for i in range(2, int(math.sqrt(num)) + 1):
        div, res = divmod(num, i)
        if res == 0: 
            result += i; 
            if i != div:
                resultado += div; 
    return resultado