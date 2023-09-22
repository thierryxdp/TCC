def busca(setor,funcionarios):
    
    for i in range(len(funcionarios)):
        if funcionarios[i][2] == setor:
            info = funcionarios[i]
            del info[2]
            lista += [info]
    return lista