def busca(setor,funcionarios):
    
    lista = []
    for i in range(len(funcionarios)):
        if funcionarios[i][2] == setor:
            lista += funcionarios[i]
    return lista