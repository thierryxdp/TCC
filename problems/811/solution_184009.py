colchao(medidas,H,L):
	medidas=[A,B,C]
	if A<L and B<H:
    	return True
    elif (A<H or C<H) and B<L:
    	return True
    elif C<L and B<H: 
    	return True
    else:
        return False