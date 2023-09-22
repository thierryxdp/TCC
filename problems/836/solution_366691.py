def busca(contatos_lista, procurar_nome):
    """dada uma string e uma matriz(o nome de um setor da empresa),
    a func̃ao retorna uma lista com os dados de todos os funcionarios daquele setor.
    string, matriz -> list"""
    contatos = list()
    for contato in contatos_lista:
        for inf_contato in contato:
            if procurar_nome in inf_contato:
                contatos.append(contato)

    return contatos