def colchao(medidas,H,L):
    """
    Identifica se um colchao passa por uma porta dadas suas dimensoes
    Parametros:
    	medidas -> list
        medidas do colchao
        H,L -> int
        altura e largura da porta
    Returns:
    	bool
        True se passar pela porta, se não False
    """
    medidas[list.index(medidas,max(medidas))]=0
    if max(medidas)<=max(H,L):
        medidas[list.index(medidas,max(medidas))]=0
        if max(medidas)<=min(H,L):
            return True
        else:
            return False
    else:
        return False