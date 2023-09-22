def colchao(medidas,H,L):
    """Função que retorna se é possivel, ou não, passar um colchão,
    dadas as medidas A, B e C, por uma porta de altura H e larguraL"""
    if medidas[1:2]>[H] and medidas[1:2]>[L]:
        return False
    elif medidas[2:-1]>[H] and medidas[2:-1]>[L]:
        return False
    else:
        return True