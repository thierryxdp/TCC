def busca(setor:str, registro_funcionarios:str) -> list:
    """Função que irá receber uma string em forma de matriz que contenha os dados dos funcionários de uma empresa (nome, registro, setor e telefone, respectivamente). A função irá receber essa matriz e o nome de um setor e retornará uma lista com os dados de todos os funcionário daquele setor. Se nenhum registro for encontrado deverá ser retornada uma lista vazia.
        str, str -> list
    
        Parameters:
        setor: string que contém o nome do setor
        registro_funcionarios: string no formato de matriz que conterá as 4 informações (nome, registro, setor e telefone) de todos os funcionários da empresa

        Returns:
        lista com os dados dos funcionários daquele setor
    """
    
    informacao_solicitada = []
    for funcionario in registro_funcionarios:
        for setores in funcionario:
            if setor in setores:
                list.append(informação_solicitada, [funcionario[0], funcionario[1], funcionario[3])])
    return informação_solicitada