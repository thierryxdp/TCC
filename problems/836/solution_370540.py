def busca(setor, dbmat):
    query = []
    
    for funcionario in dbmat:
        if funcionario[2] == setor:
            data_func = [funcionario[0],funcionario[1],funcionario[3]]
            list.append(query, data_func)
    
    return query