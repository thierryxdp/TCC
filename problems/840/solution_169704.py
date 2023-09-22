def bolos(a, b, c):
    qt_bolos = 0
    a_restante=a
    b_restante=b
    c_restante=c
    while a_restante>=2 and b_restante>=3 and c_restante>=5:
        a_restante-=2
        b_restante-=3
        c_restante-=5
        qt_bolos+=1
    return qt_bolos