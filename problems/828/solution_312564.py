def primo (n):
    p = 0
    for i in range(2,n):
    	if n % i == 0 :
        	p = p + 1
    if p > 0:
     	p = True
    else:
       	p = False

    return p