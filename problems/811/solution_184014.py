def colchao(medidas,H,L):
	A=medidas[0]
    B=medidas[1]
    C=medidas[2]
	if A<L and (B<H or C<H):
    	return True
    elif B<L and (A<H or C<H):
    	return True
    elif C<L and B<H: 
    	return True
    else:
        return False