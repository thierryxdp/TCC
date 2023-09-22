def colchao(med,h,l):
    a,b,c = med
    return a<=min(h,l) and b<=max(h,l)

def colchao(medidas:list,H:int,L:int)->bool:
    if int(medidas[1])<=H:
        return True
    elif int(medidas[1])>H:
        return False
    elif int(medidas[0])<=L:
        return True
    elif int(medidas[0])>L:
        return False