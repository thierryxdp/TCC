def colchao(med,h,l):
    a,b,c = med
    return a<=min(h,l) and b<=max(h,l)

def colchao(medidas:list,H:int,L:int)->bool:
    if int(medidas[1] or medidas[0]) <= max(H,L):
        return True
    elif int(medidas[1] or medidas[0]) > max(H,L):
        return False