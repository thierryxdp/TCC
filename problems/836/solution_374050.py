def busca(setor,matriz):
    func_encontrados = list()
    for funcionarios in matriz:
        setor_func = funcionario[2]
        if setor == stor_func:
            func_sem_setor = funcionario[:]
            del func_sem_setor[2]
            func_encontrados.append(func_sem_setor)
    return func_encontrados