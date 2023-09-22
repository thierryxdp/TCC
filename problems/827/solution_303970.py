from math import sqrt

def qtd_divisores(n):    
    """função que dado um numero inteiro retorna quantos são os seus divisores
    int --> int"""
    divs = {1,n}
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            divs.update((i,n//i))
    return len (divs)