def primo(n):
    if n < 2:
    	return False
    elif (n%2 == 0) and (n != 2):
        return False
    elif n == 2:
    	return True
    else:
        divisores = 0
        for i in range(3,n,2):
            if n%i == 0
                divisores = divisores + 1
        if divisores == 0:
            return True
        else:
            return False