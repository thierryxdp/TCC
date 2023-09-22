def bolos(A,B,C):
    "funcao que define a quantidade máxima possível para producao de bolos, dado como entrada a quantia dos insgredientes. float, float -> math floor"
    qntbolos= min(A,B,C)
    if (A<2 or(B<3)or(C<5)): qntbolos=0
    import math
    qntbolos= math.floor(min(A/2,B/3,C/5))
    return qntbolos