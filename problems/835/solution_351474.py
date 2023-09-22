def melhor_volta(matriz):
    lista = []
    for i in range (len(matriz)):
        lista.append(min(matriz[i]))
	a = min(lista)
    b = list.index(lista,a)
    c = list.index(matriz[b],a)
	resposta = (b+1,a,c+1)
    return resposta