def busca(funcionarios,setor):

    funcionarios_setor=[]

    for funcionario in funcionarios:
        if funcionario[2] == setor:
            funcionarios_setor+=funcionario.remove(setor)

    return funcionarios_setor