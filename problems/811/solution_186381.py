def colchao(medidas,H,L):
    """Cria variáveis para cada medida da cama, compara elas e excluí a maior,
    compara as duas menores medidas do colchão com as medidas da porta,
    um dos pareamento passe pela porta, retorna True, caso não, retorna False.
    lista, int, int-> boolean"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A>=B and A>=C:
        if B<=H and C<=L:
            return True
        elif C<=H and B<=L:
            return True
        else:
            return False
    elif B>=A and B>=C:
        if A<=H and C<=L:
        	return True
        elif C<=H and A<=L:
            return True
        else:
            return False
        
    else:
        if A<=H and B<=L:
        	return True
        elif B<=H and A<=L:
            return True
        else:
            return False