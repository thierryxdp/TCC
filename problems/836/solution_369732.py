def busca(setor, matriz):
   	''' Função que devolve as informações dos funcionários de um dado setor da empresa
    str, list -> list '''
    lista = []
    for i in list(range(len(matriz))):
        lista2 = []
        for j in list(range(len(matriz[0]))):
            if setor in matriz[i][j]:
                list.append(lista2, matriz[i])
        list.remove(lista2, setor)
    	list.append(lista, lista2)
    return lista