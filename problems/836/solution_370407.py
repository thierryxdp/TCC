def busca (setor, matriz):
    """Função retorna dados dos funcionarios de um determinado setor a partir de uma string com o setor e uma matriz com informações do funcionário
    str, list -> list"""
    dados = []
    for x in matriz:
        if x[2] == setor:
            list.append(dados, x[:2] + x[3:])
    if dados !=[]:
        return dados
    return []