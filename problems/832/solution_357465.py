def eh_quadrada(m):
    """
    Verifica se a matriz m é quadrada
    list -> bool
    """
    if m==[]:
        return True
    else:
        nLinhas=len(m)
    	nColunas=len(m[0])
        if nLinhas==nColunas:
            return True
        else:
            return False