def bolos(a,b,c):
    '''determina a quantidade de bolos que pode ser feita a partir de a(farinha), b(ovos) e c(colheres de leite)'''
    if round(a/2)==round(b/3)==round(c/5):
        return a/2
    elif a/2<1 or b/3<1 or c/5<1:
        return 0
    else:
        return min(round(a/2),round(b/3),round(c/5-0.7))