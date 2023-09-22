def filtra_pares(x):
    '''cria uma lista vazia, filtra os elementos dados
	em  pares e não pares, retorna os pares numa tupla
    ordenada'''
    
    f = []
    def pares_selecionados(i):
        for i in x:
        	if i%2==0:
                f.append(i)
                return f
                
    return tuple(f)