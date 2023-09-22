def primo(n):
    for i in range(1,n+1):
        if n%n==0 and n%1==0:
            if n%i==0:
                return False
            else:
                return True
    if n==1:
    	return false