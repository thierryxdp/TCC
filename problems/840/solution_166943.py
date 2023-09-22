def bolo(a,b,c):
    '''determina a quantidade de bolos que pode ser feita a partir de a(farinha), b(ovos) e c(colheres de leite)'''
    if round(a/2)==round(b/3)==round(c/5):
        return 5
    else:
        return 6