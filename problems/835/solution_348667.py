def melhor_volta(m):
    """funcao que identifica melhor corredor
    entre seis corredores de dez voltas.Entrada
    matriz 6x10,retorno-umatupla com o melhor cor
    redor o tempo e o numero da volta"""
    t=[min(m[1]),min(m[2]),min([3]),min([4]),min([5]),min([6])]
    g=min(t)
    r=list.index(t,g)+1
    return (r,g,)