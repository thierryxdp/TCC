def colchao(medidas,H,L):
    """dadas as três medidas em cm de um colchão, ordenadas da menor para a maior, na forma de uma lista e as duas
    dimensões (altura H e largura L) de uma porta, a função retorna True se o colchão passa pela porta, False caso
    contrário; list, int, int -> bool"""
    if (medidas[0] <= H and medidas[1] <= L) or (medidas[0] <= L and medidas[1] <= H):
        return True
    else:
        return False