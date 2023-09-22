def faltante(L):
	'''retorna o numero inteiro que pertence ao intervalo 1,N sem pertencer a lista de entrada L.lista->int'''
i=0
j=0
while i<len(L):
    if j!=L[i]:
        return j
    else:
        j=j+1
        i=i+1
return j