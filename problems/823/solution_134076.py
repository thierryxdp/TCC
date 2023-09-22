def faltante(L):
    ''' Dada uma lista de tamanho N-1, retorna um numero
    inteiro x que pertence ao intervalo [1,N] mas que nao
    pertence a lista de entrada
    list -> int'''
    contador=0
	local = 1
    L.sort()
    while contador < len(L)+1:
		if int(L[local]) != int(L[contador]) + 1:
			return contador
		local += 1
		contador += 1