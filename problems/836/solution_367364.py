def busca(setor,funcionarios):

    funcionarios_setor=[]

    for funcionario in funcionarios:
        if funcionario[2] == setor:
            del funcionario[2]
            funcionarios_setor+=[funcionario]

    return funcionarios_setor