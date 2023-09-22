def busca(setor, matriz):
   	''' Função que devolve as informações dos funcionários de um dado setor da empresa
    str, list -> list '''
    lista = []
    for i in list(range(len(matriz))):
        for j in list(range(len(matriz[0]))):
            if setor in matriz[i][j]:
                list.append(lista, matriz[i])
        list.remove(lista[2])
    return lista