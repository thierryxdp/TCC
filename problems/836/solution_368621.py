def busca(setor,matriz):
    '''recebe uma matriz e um setor, e retorna as informacoes de integrantes desse setor
    str, list(list) -> list'''
    
    
    for coluna in matriz:
        if setor in matriz[2]:
            return coluna
        
    return []