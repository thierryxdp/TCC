def busca(setor,matriz):
    """essa funcao recebe uma string e uma matriz e dado o nome de um setor da empresa, a funcao retorna uma lista com os dados de todos os funcion´arios daquele setor.
    str,list->list"""
    funcionarios = []
    for funcionario in matriz:
        if setor in funcionario:
            funcionarios.append(funcionario)
            del funcionarios[-1][2]
    return funcionarios