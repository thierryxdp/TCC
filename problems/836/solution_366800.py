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
    for i2 in range(len(listaRetorno)):
        for j2 in range(len(listaRetorno[0])):
            if listaRetorno[i2][j2] == string:
                del listaRetorno[i2][j2]
                
    return listaRetorno