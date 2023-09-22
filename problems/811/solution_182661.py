def colchao(medidas,h,l):
    if h*l> medidas[1]*medidas[2] and h>medidas[1] and l>medidas[2]:
        return 4==4
    elif h*l<medidas[1]*medidas[2] and (h<medidas[1] or h<medidas[2] or l<medidas[1] or l<medidas[2]):
        return 4!=5