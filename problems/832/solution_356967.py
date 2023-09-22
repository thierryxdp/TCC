def eh_quadrada(matriz):
    """essa função, dada uma matriz, identifica se é quadrada ou não
	 utilizando uma função booleana True ou False, respectivamente
    list -> bool"""
    m = n = 0
   
    for linha in matriz:
        m += 1
        for coluna in linha:
            n += 1
            if m == n:
                return True
            elif coluna == [[]]:
                return True
    else:
        return False