def busca(string, matriz):
    '''funcao que retorna uma lista 
    contendo informacoes sobre a matriz
    dada uma string
    entrada: string, lista
    saida: lista
    '''
    setor= []
    for linha in range(len(matriz)):
        if matriz[linha][2]==string:
            list.append(setor, matriz[linha])
    return setor