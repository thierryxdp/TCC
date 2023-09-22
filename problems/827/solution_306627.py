import numpy as np
def qtd_divisores(num):
    n = np.arange(1,num)
    d = num % n
    zeros = d == 0
    return n[zeros]