def faltante(L):
    ''' Dada uma lista de tamanho N-1, retorna um numero
    inteiro x que pertence ao intervalo [1,N] mas que nao
    pertence a lista de entrada
    list -> int'''
    contador=0
	local = 1
	while contador < len(L)+1:
		if L[local] != L[contador]:
			return contador
		local += 1
		contador += 1