def faltante(L):
	'''retorna o numero inteiro que pertence ao intervalo 1,N sem pertencer a lista de entrada L.lista->int'''
i=0
j=list(range(1,L[-1]+1))
if L[0]!=1:
    return 1
if L==j:
    return L[-1]+1
else:
    while i<len(L):
        if L[i+1]==L[i]+2:
            return L[i]+1