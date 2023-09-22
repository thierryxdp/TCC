import math
def qtd_divisores(n):
	d=0
	for i in range(1,999):
		if math.fbs(n)%i == 0:
			d += 1
		else:
			pass
	return d