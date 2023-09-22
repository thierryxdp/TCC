def busca(setor,dados_funcionarios):
    """retorna os dados de todos os funcionarios de um determinado setor;
    str, list(list) -> list(list)"""
    func_setor=[]
    for f in dados_funcionarios:
        for d in f:
            if setor in f:
                list.remove(f,setor)
                list.append(func_setor,f)
    return func_setor