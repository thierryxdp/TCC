def busca(string,matriz):
    """Função que dado uma string representando um setor de empresa e uma matriz com os dados dos funcionários desta empresa, retorna os dados de todos os funcionários desse setor"""
    dados = []
    for i in range(len(matriz)):
        novosdados = []
        if str.upper(string) in str.upper(matriz[i][2]):
            for f in range(len(matriz[i])):
                if str.upper(string) != str.upper(matriz[i][f]):
                    novosdados += [matriz[i][f]]  
            dados += [novosdados]
    return dados