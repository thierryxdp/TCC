# ent: list, int,int -> booleano
def colchao(medidas,H,L):
    """
    Essa função calcula se o colchão passará pela porta
    ou se não passará. 'Medidas' é uma lista onde seus 
    elementos correspondem as medidas do colchão (a,b,c).
    'H' corresponde a altura da porta e 'L' corresponde a
    largura da porta.
    """
    d=(H**2+L**2)**(1/2)
    if medidas[2]<=d:
        if medidas[1]>L:
            return false
        else:
            return true    
    return True 
	else:
        return False