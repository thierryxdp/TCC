def colchao(a,b,c,h,l):
    areacolchao = [a*b*c]
    areaporta = [h*l]
    if areacolchao>areaporta:
        return False
    if areacolchao<=areaporta:
        return True