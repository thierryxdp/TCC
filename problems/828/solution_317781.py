def primo(n):
    for i in range(2,n):
        if (n%i ==0):
        	i += 1
        else:
            return n%i==0