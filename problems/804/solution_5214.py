def filtra_pares(t):
    """retorna apenas os elementos pares da tupla original
    tuple -> tuple"""
    pares = () 
    proximo = 0
    while proximo < len(t):
        if t[proximo]%2 ==0:
            pares = pares + (t[proximo],)
            proximo += 1
	return pares