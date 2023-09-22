def busca(setor, matriz):
    """Função que recebe uma matriz e faz uma busca por setor, ou seja, dado
    um nome de um setor da empresa, a função retorna os dados de todos os 
    funcionarios daquele setor.
    str, list -> list"""
    
    retorno = []
    for contato in matriz:
        if setor in contato:
            retorno.append(contato[:2] + contato[3:])
	return retorno