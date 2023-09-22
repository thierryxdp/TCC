def faltante(lista):
    """Esta função recebe uma lista de tamanho n-1 tendo números de 1 até n e diz qual número está faltando.
    list->int"""
    resultado = 0
    N = len(lista)+1
    soma_lista = 0
    for i in range (1,N+1):
    	soma_lista += i
	return ((N*(1+N)/2)-soma_lista)