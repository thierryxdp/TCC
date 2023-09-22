def filtra_pares(x):
    '''cria uma lista vazia, filtra os elementos dados
	em  pares e não pares, retorna os pares numa tupla
    ordenada'''
    
    f = []
    def pares_selecionados(i):
        for i in x:
        	if i%2==0:
                f.append(i)
                
    return (pares_selecionados(0), pares_selecionados(1), pares_selecionados(2), pares_selecionados(3))