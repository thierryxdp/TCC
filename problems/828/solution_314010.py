def primo(n):
    a=1
    b=True
	for i in range(n-1):
		if n!=a:
            if n%a==0:
                b=False
        a=a+1
	return b