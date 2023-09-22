def bolos (A=2,B=3,C=5):
    import math
    'Calcula a quantidade de bolos que da pra fazer'
    'int, int, int -> int'
    if A<2 or B<3 or C<5:
        return 0
    elif min((A/2),(B/3),(C/5))==A/2:
        return A/2
    elif min((A/2),(B/3),(C/5))==B/3:
        return B/3
    elif min((A/2),(B/3),(C/5))==C/5:
        return C/5