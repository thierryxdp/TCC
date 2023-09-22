def busca(procurar_nome,contatos_lista):
    """dada uma string e uma matriz(o nome de um setor da empresa),
    a func̃ao retorna uma lista com os dados de todos os funcionarios daquele setor.
    string, matriz -> list"""
    contatos = list()
    for contato in contatos_lista:
        if procurar_nome in contato:
            contatos.append(contato)

    return contatos