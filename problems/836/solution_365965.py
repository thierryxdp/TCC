def busca(lista_funcionario, setor):
    """
    Função para buscar contatos em uma lista.
    :param lista_contato: lista de contatos do usuário do App.
    :param nome: o nome que deseja procurar.
    :return: uma lista com todas as informações referente aos contatos encontrados na busca.
    list, str --> list
    """
    buscador = []
    for i in lista_funcionario:
        if setor in i[2]:
            buscador.append(i)
    return buscador