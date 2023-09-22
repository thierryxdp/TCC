def faltante(listaLN):
	a = [0] + listaLN + [0]
	b = 0
	c = list(range(len(listaLN)+1)) + [listaLN] + [0]
    
    while b <= len(a):
        if c[b] != a[b]:
            return a[b-1]+1
        b += 1