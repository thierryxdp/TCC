def colchao(medidas,h,l):
    """função que recebe as dimensões de colchão (medidas), e as medidas das
    portas da sua casa em altura (h) e largura (l), todas em centímetros. E
    que retorna se o colchão com as medidas enviadas vão passara através das
    portas da casa;
    lista, int,int->bool"""
    medida_colchao = medidas
    medida_porta = list((h,l))
    medida_colchao2 = medidas[1:]
    
    if medida_colchao<medida_porta:
        return True
    elif medida_colchao2>medida_porta:
        return False
    else:
        return False