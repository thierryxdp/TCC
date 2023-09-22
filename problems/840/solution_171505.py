def receita_minima(A,B,C):
    """receita minima do bolo"""
    if (A<2 or (B<3) or (C<5)): bolos=0
        import math 
        bolos= math.floor(min(A/2,B/3,C/5))
        return bolos