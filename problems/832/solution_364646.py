def eh_quadrada(lista):
    """
    Essa função define se a matriz é quadrada ou não
    list -> bool
    """
    if lista == []:
    	return len(lista)==[]
    else:
       	return len(lista)==len(lista[0])