def filtra_pares(t):
    a=()
    b=0
    while b<=len(t):
    	if t[b]%2==0:
        	a=a+t[b]
            b+=1
        else:
            b+=1
        return a