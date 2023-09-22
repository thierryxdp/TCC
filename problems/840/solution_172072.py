import math
def bolos(A,B,C):
    
    if min(A,B,C) == A:
        if (A%2==0):
        	qtd_bolos = A/2
        	return qtd_bolos
        else:
            qtd_bolos = 0
            return qtd_bolos
    elif min(A,B,C) == B:
        if (B%3==0):
        	qtd_bolos = B/3
            return qtd_bolos
       	else:
        	qtd_bolos = 0 
            return qtd_bolos
    elif min(A,B,C) == C:
        if (C%5==0):
        	qtd_bolos = C/5
        	return qtd_bolos
        else:
            qtd_bolos = 0
            return qtd_bolos