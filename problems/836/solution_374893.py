def busca(setor, matriz):
    '''list(list) --> list'''
    func_encontrados = list()
    for func in matriz:
        setor_func = func[2]
        
        if setor == setor_func:
            func_sem_setor = func[:]
            
            del func_sem_setor[2]
            
            func_encontrados.append(func_sem_setor)
    return func_encontrados