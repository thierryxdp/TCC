def colchao(medidas,H,L):
    """Essa função retorna pro meio de True e False se o colchão
    comprado passará pela porta. como entrada temos uma lista,e dois
    inteiros e como saída temos um booleano;
    list,int,int->bool"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=L and B<=H:
        return True
    if B<=L and B<=H:
        return True
    else:
        return False