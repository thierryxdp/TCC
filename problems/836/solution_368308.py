def busca (setor, matriz):
    """Recebe uma matriz com informações sobre cada funcionario
    e um setor da empresa, e retorna as informações de cada
    funcionário que trabalha em cada setor.
    str, list -> list"""
    informacoes = []
    for funcionario in matriz:
        if setor in funcionario:
            del funcionario[2]
            list.append (informacoes, funcionario)
    return informacoes