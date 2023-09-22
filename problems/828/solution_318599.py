def primo(n):
	ePrimo = 0
	for i in range(1, (n + 1)):        
  		if n % i == 0:
    		ePrimo += 1
    
		if ePrimo  == 2:
  			return True
		else:
  			return False