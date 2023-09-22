def colchao(medidas,H,L):
    """returna True se o colchao passa pela porta e False caso o colchao não passe pela porta.
    Parametros:
    Entrada:list,int,int
    Saída:Booleano"""
    a=medidas[0]
    l=medidas[1]
    c=medidas[2]
    if (a and b and c)<=(H and L):
    	return True
    if (a and b and c)<=H and ((a and l) or (a and c) or (c and l))<=L:
        return True
	if (a and b and c)<=L and ((a and l) or (a and c) or (c and l))<=H:
        return True