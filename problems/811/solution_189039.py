def colchao(med,h,l):
    a,b,c = med
    return a<=min(h,l) and b<=max(h,l)

def colchao(medidas:list,H:int,L:int)->bool:
    
    
    return int(medidas[1] or medidas[0]) <= max(H,L)