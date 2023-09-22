def busca(setor, matriz):
    '''
    dada uma matria contendo apenas str e uma str retorna
    todas as linhas que contem a str dada como argumento 
    com seus respectivos elementos (exceto a propria str)
    dados de entrada: str, list
    retorna: list
    '''
    acumulador = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(acumulador,[matriz[i][0],matriz[i][1],matriz[i][3]])
  	return acumulador