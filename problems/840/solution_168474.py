def bolos(A,B,C):
    """Função que retorna a quantidade máxima de bolos que João consegue fazer."""
    a=A/2
    b=B/3
    c=C/4
    r=min(a,b,c)
    return math.floor(r)