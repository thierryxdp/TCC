def primo(n):
    b=True
	for i in range(n):
		if i not in"0,1":
            if n%i==0:
                b=False
	return b