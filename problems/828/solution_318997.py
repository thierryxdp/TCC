def  primo(n):
    if n == 2 or (n != 1 and n % 2 ==1):
      	return True
    else:
        return False
	i = 3
	while i < n // 2:
        if n % i == 0:
            return False 
        i +=2