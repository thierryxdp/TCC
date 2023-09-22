def bolos (A=2,B=3,C=5):
    import math
    'int, int, -> int'
    if A<2 or B<3 or C<5:
        return 0
    elif B==3 and C==5 or A==2 and B==3 or A==2 and C==5:
        return 1
    else:
        return math.floor()