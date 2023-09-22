def colchao(medidas,H,L):
    """Função analisa se um colchão é capaz de passar por uma porta de altura H e largura L, dados: as medidas do colchão e as medidas da porta;
    list[int,int,int],int,int->bool"""
    if  min(H,L)>=medidas[0] and max(H,L)>=medidas[1]:
        return True
    else:
        return False