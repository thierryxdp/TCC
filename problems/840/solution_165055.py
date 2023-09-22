def bolos(a,b,c):
    lista = []
	a1 = a//2
    b1 = b//3
    c1 = c//5
    lista.append(a1,b1,c1)
    lista.sort()
    return lista[0]