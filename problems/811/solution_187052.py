def colchao(medidas,H,L):
    """essa função recebe como entrada as medidas de um colchão e de uma porta e calcula se esse colchao consegue ou não passar por essa porta;
    list,int,int--->bool"""
    x=int((medidas[0])*(medidas[1])*(medidas[2]))
    if x<=2*H+2*L:
        return True
    else:
        return False