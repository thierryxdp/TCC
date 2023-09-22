def faltante(l):
    i = max(l)
    lista = [5,1,2,3,4,90]
    while min(l) < i:
        i = i - 1
        if i in l:
    	return i