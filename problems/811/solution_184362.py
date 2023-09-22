def colchao(medidas, H, L):
    """
    """
    entrada = input("A B C").split()
    A, B, C = int(entrada[0], int(entrada[1],int(entrada[2])
    	if A >= 1 and A <= 25 and B >= 1 and B <= 200 and C >= 1 and C <= 220:
    		return True
    	else:
        	return False
    entrada = input("Porta").split()
    H, L = int(entrada[0], int(entrada[1])
    if H >= 1 and H <= 200 L >= 1 and L <=100:
    	return True
    else:
       	return False 
     if (A and B) > (H and L) or (A and C) > (H and L) or (B and C) > (H and L):
     	return True
     else:
        return False