from math import factorial
def soma_h():
    '''funcao que calcula a soma, none->float'''
    n=0
    for i in range(10):
        n+=((-1)**(i)*(10-i))/factorial(i+1)
        return round(n,2)