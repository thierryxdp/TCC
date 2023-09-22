def colchao(medidas,H,L):
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    
    if (a<=H and b<=L) or (a<=L and b<=H)
    	return True
    elif(a<=H and c<=L) or (a<=L and c<=H):
        return True
    elif(b<=H and c<=L) or (b<=L and c<=H):
        return True
    else:
        return False