def colchao(medidas,h,l):
    """função que recebe as dimensões de colchão (medidas), e as medidas das
    portas da sua casa em altura (h) e largura (l), todas em centímetros. E
    que retorna se o colchão com as medidas enviadas vão passara através das
    portas da casa;
    lista, int,int->bool"""
    altura = medidas[0]
    comprimento = medidas[1]
    largura = medidas[2]
    face1_colchao = altura*comprimento
    face2_colchao = altura*largura
    face3_colchao = largura*comprimento
    area_colchao = (2*face3_colchao)+(2*face2_colchao)
    area_porta = (h*l*l)
    
    if ((area_porta)>(area_colchao)):
        return True
    else:
        return False