def busca(setor, matriz):
    '''
    Inicia uma lista vazia e tira uma cópia da matriz inicial
    para não apagar os dados originais. Varre as sub listas
    de M e verifica se a coluna "setor" corresponde ao setor
    pedido. Caso sim, exclui essa coluna e insere a sub lista
    modificada na nova lista. Depois retorna a nova lista.
    '''
    L = []; M = matriz.copy()
    
    for x in M:
        if x[2] == setor:
            del x[2]
            L.append(x)
	return L