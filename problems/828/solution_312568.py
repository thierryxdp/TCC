def primo (n):
    p = 0
    primos = True
    for i in range(2,n):
    	if n % i == 0 :
        	p = p + 1
    if p > 0:
     	primos = False

    return primos