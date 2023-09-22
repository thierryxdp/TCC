def primos(n):
    divisores = 2
    for i em range(3,n/2,2):
        if n % i = 0:
            divisores +=1
        	if divisores > 2:
                return False
    return True