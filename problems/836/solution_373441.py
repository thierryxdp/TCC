def busca(setor,matriz):
    """"
    	Função que faz uma busca por setor na matriz, 
        retornando os dados de todos os funcionários 
        daquele setor.
        string,list[list] -> list[list]
    """
    retorno = []
    for linha in matriz:
        if setor in linha:
            linha.pop(2)    
            retorno.append(linha)
    return retorno