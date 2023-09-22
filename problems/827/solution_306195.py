import math
def qtd_divisores(n):
    """Soma a quantidade de divisores de um determoinado n ;int=>int"""
    div = [1]
    if n<0:
    	return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
        	div.extend([i,n/i])
    div.extend([n])
    return len(list(set(div)))