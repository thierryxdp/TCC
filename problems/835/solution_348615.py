def melhor_volta(m):
    """funcao que identifica melhor corredor
    entre seis corredores de dez voltas.Entrada
    matriz 6x10,retorno-umatupla com o melhor cor
    redor o tempo e o numero da volta"""
    m[0]=c1,m[1]=c2,m[2]=c3,m[3]=c4,m[4]=c5,m[5]=c6
    t=[min(m[0]),min(m[1]),min([2]),min([3]),min([4]),min([5])]
    g=min(t)
    return g