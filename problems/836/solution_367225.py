def busca(buscar,matriz):
    """calculo e retorno de uma funçao que busque numa matriz dados."""
    dados = []
    for nome, registro, setor, fone in matriz:
        if setor == buscar:
             dados.append([nome, registro, fone])
    return dados