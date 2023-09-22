def melhor_volta(m):
    """funcao que identifica melhor corredor
    entre seis corredores de dez voltas.Entrada
    matriz 6x10,retorno-umatupla com o melhor cor
    redor o tempo e o numero da volta"""
    t=[min(m[0]),min(m[1]),min([2]),min([3]),min([4]),min([5])]
    g=min(t)
    return ((list.index(t,g)),g,)