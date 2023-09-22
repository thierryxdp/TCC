def qtd_divisores(n):
	import math
    divs = [1]
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))