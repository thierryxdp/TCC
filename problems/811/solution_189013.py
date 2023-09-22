def colchao(medidas,H,L):
    """função onde as medidas é uma lista com os tamanhos inteiros A, B e C, e H e L são os tamanhos inteiros da altura e largura da porta;
    int, int, int -> int"""
    if colchao(A,B,C) <= porta(H,L):
        return (True)
    else:
        return (False)