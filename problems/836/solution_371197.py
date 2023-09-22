def busca(setor:str,matriz:list)->list:
    matriz_do_setor = filter(lambda x: setor in x, matriz)
    map(lambda x: x.remove(setor),matriz_do_setor)
    return matriz_do_setor