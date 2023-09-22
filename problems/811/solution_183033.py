colchao(medidas,H,L):
    """Função analisa se um colchão é capaz de passar por uma porta de altura H e largura L, dados: as medidas do colchão e as medidas da porta;
    list[int,int,int],int,int->bool"""
    if medidas[0]=<min(H,L) and medidas[1]=<max(H,L):
        return True
    else:
        return False