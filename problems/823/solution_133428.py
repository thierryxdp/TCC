def faltante(l):
    x = 1
    lx = []
    while x < len(l)+1: 
    	lx.append(x)
        x += 1
    i = 0
    while i < len(l):
        if lx[i] != l[i]:
            return lx[i]
        i += 1