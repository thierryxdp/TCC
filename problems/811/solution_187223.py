def colchao(medidas,H,L):
    """Função que dados as medidas de um colchão e altura e largura da porta, retorna se o colchão passa pela porta. list,int,int --> bool"""
    if medidas[1]<=H:
        return 1==1
    if medidas[1]>H and medidas[2]<L:
        return 1==1
    if medidas[2]>H and medidas[2]>L:
        return 1==0