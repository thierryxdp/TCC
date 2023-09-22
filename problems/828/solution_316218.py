def primo(n):
    p = [2,3,5,7,11,13,17,19,23,29]
    while n in p:
        return True
    while n not in p:
        if n % 2 == 0:
            return False
        if n % sqrt(n) == 0:
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
        if n % 23 == 0:
            return False
        if n % 29 == 0:
            return False
        if n % 31 == 0:
            return False
        if n % 37 == 0:
            return False
        else:
            return True
        ###41 == 0:
        #43
        #47
        #53
        #59
        #61
        #67
        #71