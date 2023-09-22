def busca(setor,matriz):
    """Funcao que, dado um setor e uma matriz, retorna os dados de todos os funcionarios daquele setor
    string,list -> list"""
    lista=[1]
    for funcionario in matriz:
        if setor in funcionario:
            lista=lista+[[funcionario[0]]+[funcionario[1]]+[funcionario[3]]]
    return lista