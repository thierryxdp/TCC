def busca(setor, matriz):
    """str, list(list) -> list(list)"""
    """retorna os dados de todos os funcionários daquele segor"""
    
    B = []
    M = []
    
    for m in matriz:
        if setor in m:
            for e in m:
                if e != setor:
                    list.append(M,e)
                    pass
                pass
            list.append(B,M)
            M = []
            pass
        pass
    return B