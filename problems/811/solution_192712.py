def colchao(col, h, l):
    """Função que, dadas as dimensões de um colchão, verifica se ele passa pela porta. list + int + int -> bool"""
    if col[1] <= h or col[1] <= l:
        return True
    elif col[2] <= h or col[2]<= l:
        return True
    else:
        return False