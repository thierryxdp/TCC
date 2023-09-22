def busca(setor, lista_funcionario):
    """
    Função para buscar as informações dos funcionários a partir do seu setor.
    setor: é o setor da empresa que se deseja pesquisar os funcionários.
    lista_funcionario: é a lista com o cadastro de todos os funcionários da empresa.
    str, list(list) --> list(list)
    """
    buscador = []
    listagem = lista_funcionario.copy()
    for i in listagem:
        if setor == i[2]:
            del i[2]
            buscador.append(i)
    return buscador