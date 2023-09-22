def eh_quadrada(m):
    """
		Rterona se a matriz é quadrada ou não.
        list -> bool
    """
    if len(m) == len(m[0]) or m == []:
		return True
    else:
        return False