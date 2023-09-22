def eh_quadrada(matriz):
    cont_lin = 0
    if not matriz:
        return True
    for linha in matriz:
        cont_lin += 1
        cont_col = 0
        for elemento in linha:
            cont_col += 1
	if cont_lin == cont_col:
        return True
    else:
        return False