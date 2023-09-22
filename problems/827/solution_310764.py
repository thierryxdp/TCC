def qtd_divisores(n):
	x, mult = 1,1
    l = []
	while(x<n):
		if(n % x == 0):
			l.append(x)
			mult += 1
		x+=1
	else:
		return len(l)