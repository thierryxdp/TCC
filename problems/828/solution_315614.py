def primo(num):
	for i in range(2, num//2):
		if (num % i) == 0:
			return False
   	 	break
	else:
	return True
	else:
	return False