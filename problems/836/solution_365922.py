def busca(string,matriz):
    """Retorna uma lista com todos os dados dos funcionarios de um setor que foi buscado;
    str, list -> list"""

    linhas = len(matriz)
    colunas = len(matriz[0])
    listaRetorno = []

    for i in range(linhas):
        for j in range(colunas):
            if string in matriz[i][j]:
                listaRetorno.append(matriz[i])
    	list.remove(listaRetorno[i], string)
    return listaRetorno