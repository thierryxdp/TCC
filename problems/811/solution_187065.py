def colchao(medidas,H,L):
    """essa função recebe como entrada as medidas de um colchão e de uma porta e calcula se esse colchao consegue ou não passar por essa porta;
    list,int,int--->bool"""
    X=int(medidas[1])
    ih H>=X:
        return True
    else:
        return False