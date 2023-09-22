def busca(setor,matriz):
    """Esta função recebe uma lista n x 4 sómente de strings e  uma palavra que deve ser igual a da 3 terceira da linha que você quiser ter a informação e retorna todas as linhas que tem na coluna 3 a string que foi dada na entrada 
    str, list -> list"""
    c = 0
    l = []
    lista = []
    if setor == matriz[c][2]:
    	while c < len(matriz):
        	if setor == matriz[c][2]:
            	lista.append(matriz[c][0])
            	lista.append(matriz[c][1])
            	lista.append(matriz[c][3])
            	l.append(lista)
    		c += 1
    	return l
    else:
        return []