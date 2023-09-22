def colchao(medidas,H,L):
    """essa função recebe como entrada as medidas de um colchão e de uma porta e calcula se esse colchao consegue ou não passar por essa porta;
    list,int,int--->bool"""
    x=int((2*medidas[0]*medidas[1])+(2*medidas[0]*medidas[2])+(2*medidas[1]*medidas[2]))
    if x<=H+H+L+L:
        return True
    else:
        return False