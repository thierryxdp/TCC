def busca(area, matriz):

    '''Função que recebe uma string e uma matriz e faça uma busca por setor,
ou seja, dado o nome de um setor da empresa, a função retorna uma lista com
os dados de todos os funcionários daquele setor.
str, list -> list'''
    
    resultado = []
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if area.lower() == matriz[linha][coluna].lower():
                dados = matriz[linha].copy()
                dados.pop(dados.index(dados[coluna]))
                resultado.append(dados)
    return resultado