def colchao(medidas,H,L):
	A=medidas[0]
    B=medidas[1]
    C=medidas[2]
	if A<L and B<H:
    	return True
    elif (A<H or C<H) and B<L:
    	return True
    elif C<L and B<H: 
    	return True
    else:
        return False