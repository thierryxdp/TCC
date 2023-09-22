def busca(busca: str, matriz: List[List[str]]) -> List[list]:
    """funçao que recebe uma matriz fazendo uma busca por ela  e retorna os dados do funcionario daquele setor
    string, lista -> lista"""
    dados = []
    for nome, registro, setor, fone in matriz:
        if setor == busca:
            dados.append([nome, registro, fone])
    return dados