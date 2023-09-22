def colchao(med,h,l):
    a,b,c = med
    return a<=min(h,l) and b<=max(h,l)

def colchao(medidas:list,H:int,L:int)->bool:
    if int(medidas[1]) <= H and H>L:
        return True
    elif int(medidas[1])> H and H>L:
        return False
    elif int(medidas[0]) <= L and H>L:
        return True
    elif int(medidas[0]) > L and H>L:
        return False
    if int(medidas[1]) <= L and H<L:
        return True
    elif int(medidas[1])> L and H<L:
        return False
    elif int(medidas[0]) <= H and H<L:
        return True
    elif int(medidas[0]) > H and H<L:
        return False