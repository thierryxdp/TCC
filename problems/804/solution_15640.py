def filtra_pares(tupla):
    """
    	Função que recebe quatro números e retorna apenas os pares 
        na ordem em que se encontravam.
        int,int,int,int->tupla
    """
    if tupla[0]%2==0:
        return (tupla[0],)
    elif tupla[1]%2==0:
        return (tupla[1],)
    elif tupla[2]%2==0:
    	return (tupla[2],)
    elif tupla[3]%2==0:
        return (tupla[3],)