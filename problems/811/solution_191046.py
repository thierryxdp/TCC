def colchao(medidas,H,L):
    """função que define se o colchão novo conseguira passar pela porta, dada as medidas do colchão e a altura e largura da porta;
    lista, int, int -> str"""
    altura = medidas[1]
    largura = medidas[2]
    if altura <= H:
        return "True"
    if largura <= L:
        return "True"
    else:
        return "False"