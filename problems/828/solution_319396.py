def primo(n):
    if n == 2:
        return True
    if n ==0 or n ==1:
        return False
    for i in range(2,n+1):
        if n % i == 0:
        	return False
    return True