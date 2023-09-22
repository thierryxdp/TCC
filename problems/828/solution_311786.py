def primos(n):
	p=0
	for i in range(2,n+1):
		if ((n%i) == 0):
			p=p+1
	if p>2:
		return False
	return True