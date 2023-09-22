def busca(setor,matriz):
2	    '''
3	    '''
4	    lista_dados = []
5	    for i in range(len(matriz)):
6	        for j in range(len(matriz[0])):
7	            if setor == matriz[i][j]:
8	                lista_dados.append(matriz[i])
9	    return lista_dados