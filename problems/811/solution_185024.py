def colchao(medidas,h,l):
    """função que recebe as dimensões de colchão (medidas), e as medidas das
    portas da sua casa em altura (h) e largura (l), todas em centímetros. E
    que retorna se o colchão com as medidas enviadas vão passara através das
    portas da casa;
    lista, int,int->bool"""
    
    if (medidas[1]>h):
        return False
    elif (medidas[2]>l):
        return False
    elif (medidas[1]<h):
        return True
    else:
        return True