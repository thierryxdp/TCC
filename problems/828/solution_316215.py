def primo(n):
    if n % 2 == 0:
        return False
	if n % 3 == 0:
	    return False
	if n % 5 == 0:
	    return False
	if n % 7 == 0:
	    return False
    if n % 11 == 0:
	    return False
	if n % 13 == 0:
        return False
    if n % 17 == 0:
        return False
    if n % 19 == 0:
        return False
	else:
	    return True