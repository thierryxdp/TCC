from math import factorial
'''Retorna o valor da soma S;
None -> float'''
def soma():
    s = 0
    for i in range(10):
        s += (-1)**i * (10-i) / factorial(i+1)
    return s