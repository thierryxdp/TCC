def colchao(medidas,H,L):
    """retorna se o colchao passa pela porta.entra medidas do colchao
    da menor para a maior(medidas),altura da porta(H)
    e largura da porta(L);list[int,int,int],int,int->booleano"""
    if L>=medidas[0] and H>=medidas[1] or L>=medidas[1]:
        return True
    else:
        return False