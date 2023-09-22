def colchao(medidas,H,L):
    "a função calcula colchao que tem dimensoes A x B x C, a forma de um paralelepipedo reto retangulo: list,float,float->bool"
    if medidas[1]>L and medidas[1]>H:
        return False
    else:
        return True