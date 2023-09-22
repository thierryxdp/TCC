def busca(setor,matriz):
    '''recebe uma matriz e um setor, e retorna as informacoes de integrantes desse setor
    str, list(list) -> list'''
    
    lista = []
    
    for coluna in matriz:
        for elemento in matriz:
            if elemento == setor:
                lista = list.append(coluna,lista)
    
    return lista