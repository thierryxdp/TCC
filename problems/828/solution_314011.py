def primo(n):
    a=1
    b=True
	for i in range(n):
		if n!=a:
            if n%a==0:
                b=False
        elif n==a:
            if n%a==0:
                b=True
        a=a+1
	return b