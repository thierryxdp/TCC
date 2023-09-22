def filtra_pares(A, B, C, D):
    if A%2 == 0:
        if B%2 == 0:
            if C%2 == 0:
                if D%2 == 0:
                    return (A, B, C, D)
    elif B%2 =! 0:
        if A%2 == 0:
        	if C%2 == 0:
            	if D%2 == 0:
                	return(A, C, D)
    elif C%2 =! 0:
        if A%2 == 0:
            if B%2 == 0:
                if D%2 == 0:
                    return(A, B, D)
    elif D%2 =! 0:
        if A%2 == 0:
            if B%2 == 0:
                if C%2 == 0:
                    return(A, B, C)