def qtd_divisores(n):
    """função que conte quantos divisores um numero tem.Este numero será passado como entrada
    int -> int
    """
    for i in range(1, n//2+1):
        if n%i == 0:
            yield i
    	yield n
    
   	return list(qtd_divisores(n))