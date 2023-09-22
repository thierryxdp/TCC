def busca(setor,matriz):
    '''Função que realiza uma busca, na matriz fornecida, pelos funcionários
pertencentes ao setor informado e retorna uma lista com os dados de todos os
funcionários desse setor
    str, list -> list
    '''
    contador = 0
    resposta = []
    for i in range(len(matriz)):
        if  setor == matriz[i][2]:
            resposta.append(matriz[i])
            resposta[contador].remove(setor)
            contador += 1
    return resposta