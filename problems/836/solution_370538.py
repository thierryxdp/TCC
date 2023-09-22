def busca(setor, dbmat):
    query = [1]
    
    for funcionario in dbmat:
        if funcionario[2] == setor:
            list.append(funcionario, query)
    
    return query