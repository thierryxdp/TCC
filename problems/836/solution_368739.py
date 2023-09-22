def busca(matriz, setor):
    """Função que buscar os dados de um contato salvo: recebe como entrada a lista de contatos e uma
    string referente ao nome buscado e retorna uma lista de contatos que tem o nome buscado.
    list, str -> list"""
    funcionarios = []
    for i in matriz:
        if i[3] == setor:
            funcionarios.append(i)
    return funcionarios