def faltante(l):
    lista = [5,1,2,3,4,20]
    f = 0
    i = max(l)
    while 1 < i:
        i = i - 1
        if not i in l:
            f = i
    if f == 0:
    	f = max(l) + 1         
    return f