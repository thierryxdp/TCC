def bolos(A,B,C):
    """função que define a quantidade máxima de bolos dadas coordenadas A,B,C.
    float,float,float->int"""
    return max((A>=2)+(B>=3)+(C>=5))