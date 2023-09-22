def colchao(medidas,H,L):
    """
    Essa função calcula se o colchão passará pela porta
    ou se não passará. 'Medidas' é uma lista onde seus 
    elementos correspondem as medidas do colchão (a,b,c).
    'H' corresponde a altura da porta e 'L' corresponde a
    largura da porta.
    Parametro de Entrada: list, int, int
    Valor de Retorno: bool
    """
    
    if medidas[0]<=H and medidas[1]<=L:
        return True 
    if medidas[0]<=H and medidas[2]<=L:
        return True
    if medidas[1]<=H and medidas[0]<=L:
        return True 
    if medidas[1]<=H and medidas[2]<=L:
        return True
    if medidas[2]<=H and medidas[0]<=L:
        return True 
    if medidas[2]<=H and medidas[1]<=L:
        return True
    else:
        return False