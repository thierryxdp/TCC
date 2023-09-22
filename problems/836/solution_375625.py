def busca(setor, matriz):
    ''' funcao que recebera uma matriz e busca por setor os dados de cada 
    funcionario'''
    lista_retorno = []
    for i in matriz:
        if i[2] == setor:
            lista_retorno.append(i[0:2] + i[3:])
        return lista_retorno