def melhor_volta(matriz):
    lista = []
    for i in range (len(matriz)):
        lista.append(min(matriz[i]))
	a = min(lista)
    b = lista.index(a)
    c = lista.index(matriz[b],a)
    return [b,a,c]