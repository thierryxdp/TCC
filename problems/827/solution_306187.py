import math
def qtd_divisores(n):
    n= int and n>0
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
        	divs.extend([i,n/i])
    divs.extend([n])
    return len(list(set(divs)))