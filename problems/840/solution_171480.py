def bolos(Xicaras, Ovos, Colheres):
    a = Xicaras//2
    b = Ovos//3
    c = Colheres//5
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    elif c<=a and c<=b:
        return c