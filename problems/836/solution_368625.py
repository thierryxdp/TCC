def busca(setor,matriz):
    '''recebe uma matriz e um setor, e retorna as informacoes de integrantes desse setor
    str, list(list) -> list'''
    
    lista = []
    
    for coluna in matriz:
        if setor == coluna[2]:
            return lista.append(coluna)
        
    return lista