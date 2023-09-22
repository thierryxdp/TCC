def bolos(A,B,C):
	''' Função que determina qual a quantidade máxima de bolos que João pode fazer'''  
	import math
    q = min(A/2,B/3,C/5)
    c =math.trunc(q)
    return c