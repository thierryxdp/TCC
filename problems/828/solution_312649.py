def primo(n):
    for i in range(2,n):   
        if n%1==0 and n%n==0:
            if n%i==0:
                if i<n:
                    return False
        	else:
           		return True