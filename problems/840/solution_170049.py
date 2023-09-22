def bolos (A=2,B=3,C=5):
    import math
    'int, int, -> int'
    if A<2 or B<3 or C<5:
        return 0
    else:
        return math.floor((A*B*C)/(30))