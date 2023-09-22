def colchao(medidas,H,L):
    """Função que calcula se é possível passar com o colchão pela porta;
    list,int,int -> bool"""
    if medidas[1]=H:
        return True
    elif medidas[1]<H:
        return True
    else medidas[1]>H:
        return False