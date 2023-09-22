def colchao(medidas,h,l):
    """função que recebe as dimensões de colchão (medidas), e as medidas das
    portas da sua casa em altura (h) e largura (l), todas em centímetros. E
    que retorna se o colchão com as medidas enviadas vão passara através das
    portas da casa;
    lista, int,int->bool"""
    medida_colchao = medidas[1:]
    medida_porta = list((h,l))
    
    if medida_colchao>medida_porta:
        return False
    elif medidas[2]<l:
        return True
    else:
        return True