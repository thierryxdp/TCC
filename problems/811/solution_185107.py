def colchao(medidas,h,l):
    """função que recebe as dimensões de colchão (medidas), e as medidas das
    portas da sua casa em altura (h) e largura (l), todas em centímetros. E
    que retorna se o colchão com as medidas enviadas vão passara através das
    portas da casa;
    lista, int,int->bool"""
    face1_colchao = medidas[0]*medidas[1]
    face2_colchao = medidas[0]*medidas[2]
    area_colchao = face1_colchao+face2_colchao
    area_porta = (h*l)
    
    if (area_colchao)>(area_porta):
        return False
    else:
        return True