def intercala(lista1,lista2):
    '''Função que dadas duas listas(lista1 e lista2) gera uma nova lista que é formada intercalando os elementos das duas listas anteriores(lista1 e lista2)
       parâmetros de entrada: list, list
       valor de retorno: list'''
    return str.format("[{0},{3},{1},{4},{2},{5}]",str(lista1[0]),str(lista1[1]),str(lista1[2]),str(lista2[0]),str(lista2[1]),str(lista2[2]))