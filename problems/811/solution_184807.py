def colchao(medidas,h,l):
    """ Essa função retorna se é possível passar com o colchão novo pela porta da casa."""
    if medidas[1]<l or medidas[2]<h or medidas[1]<h:
        return True
    else:
        return False