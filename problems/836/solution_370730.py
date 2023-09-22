def busca(setor, matriz):
    """ Função que recebe uma matriz com os dados dos
    funcionários da empresa e dado o nome do setor da 
    empresa, retorna todos os funcionários do mesmo"""
    dados = []
    for funcionario in matriz:
        linha = []    
        if setor in funcionario[2]:
            list.append(linha,funcionario[0])
            list.append(linha,funcionario[1])
            list.append(linha,funcionario[3])
            dados = dados + [linha]   
    return dados