def primo(n):
    divisores = 2
    if n % 2 == 0:
        return false
    for i in range(3,n,2):
        if n % i == 0:
            divisores +=1
        	if divisores > 2:
                return False
    return True