import math
def qtd_divisores(n):
	d=0
	for i in range(1,999):
        if n>0:
            if n%i == 0:
                d += 1
            else:
                 pass
	return d