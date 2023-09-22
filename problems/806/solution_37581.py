# 7) Questão da OBI.

def colisao(ret1,ret2):
    '''tupla, tupla -> bool'''
    xi1 = int(ret1[0])
    yi1 = int(ret1[1])
    xs1 = int(ret1[2])
    ys1 = int(ret1[3])
    xi2 = int(ret2[0])
    yi2 = int(ret2[1])
    xs2 = int(ret2[2])
    ys2 = int(ret2[3])
    possibilidade1 = (xs1 >= xi2 and (yi2 <= ys1 or yi2 <=  yi))
    possibilidade2 = (xi2 <= xi1 and (yi2 >= yi1 or yi1 <= ys2))
    return  possibilidade1 or possibilidade2