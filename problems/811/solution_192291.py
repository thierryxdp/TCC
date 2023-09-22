def colchao(medidas,H,L):
    """Função que informa se o colchão passa pela porta dados
as medidas do colchao, a altura da porta e a largura; list,int,int -> bool"""
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    passou = True

    if b>H:
        passou=False
        return passou
    if b<H:
        return passou
    else:
        return passou