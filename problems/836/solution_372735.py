def busca(setor, matriz):
    """Recebe um setor e uma matriz de informações de funcionários
    de uma empresa, retornando todos os dados dos funcionários
    daquele setor;
    str, list -> list"""
    encontrados = []
    for linha in matriz:
        if linha[2] == setor:
            encontrados.append(linha)
    return encontrados