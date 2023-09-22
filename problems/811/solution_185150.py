def colchao(medidas,h,l):
    """função que recebe as dimensões de colchão (medidas), e as medidas das
    portas da sua casa em altura (h) e largura (l), todas em centímetros. E
    que retorna se o colchão com as medidas enviadas vão passara através das
    portas da casa;
    lista, int,int->bool"""
    altura_colchao = medidas[0]
    comprimento_colchao = medidas[1]
    largura_colchao = medidas[2]
    
    if (comprimento_colchao>h):
        if (largura_colchao>l):
        return False
    
    else:
        return True