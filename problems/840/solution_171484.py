def bolos(A,B,C):
    "funcao que define a quantidade máxima possível para producao de bolos, dado como entrada a quantia dos insgredientes. float, float -> int"
    qntbolos= min(A,B,C)
    if A<2: qntbolos=0
    if B<3: qntbolos=0
    if C<5: qntbolos=0
    import math
    return math.floor(qntbolos)