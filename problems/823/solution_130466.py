def faltante(L):
    """Essa funcao, dada uma lista L de tamanho N - 1 contendo apenas
	 numeros inteiros de 1 a N, retorna o numero inteiro X que
	 pertence ao intervalo [1, N], mas não pertence a lista de entrada L"""
    i = 1
    final = 0
    
    while i <= len(L):
        if i not in L:
            final = final + i
        i = lista[i-1]+1
    if final == 0:
        final += len(L)+1
    return final