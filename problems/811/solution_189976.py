def colchao(medidas, H, L):
    """ docs
    list, int, int -> bool """

    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    cont = 0
    
    if A <= H:
        cont = cont + 1
    if A <= L:
        cont = cont + 1
    if B <= H:
        cont = cont + 1
    if B <= L:
        cont = cont + 1
    if C <= H:
        cont = cont + 1
    if C <= L:
        cont = cont + 1
    if cont >= 2:
        return True
    else:
        return False