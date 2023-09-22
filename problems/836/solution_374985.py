def busca(setor, matriz):
    """Função que recbe uma matriz com os dados dos 
    dos funcionários de uma empresa e dado o setor,
    retorna quais funcionários trabalham nela
    Entrada : str, list
    Saída: list """
    dados = []
    for funcionario in matriz:
        linha = []    
        if setor in funcionario[2]:
            list.append(linha,funcionario[0])
            list.append(linha,funcionario[1])
            list.append(linha,funcionario[3])
            dados = dados + [linha]   
    return dados