def busca(string,matriz):
    """Retorna os dados de todos os funcionarios do setor buscado;
    str,list -> list"""

    linhas = len(matriz)
    colunas = len(matriz[0])
    listaRetorno = []
    
    for i in range(linhas):
        for j in range(colunas):
            if string in matriz[i][j]:
                listaRetorno.append(matriz[i])
        if len(listaRetorno) == 2:
            del listaRetorno[0][2]
            del listaRetorno[1][2]
        if len(listaRetorno) == 1:
            del listaRetorno[0][2]
                
    return listaRetorno