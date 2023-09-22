def busca(setor,matriz):
    '''recebe uma matriz e um setor, e retorna as informacoes de integrantes desse setor
    str, list(list) -> list'''
    
    lista = []
    sublista = []
    
    for coluna in matriz:
        if setor == coluna[2]:
            sublista.append(coluna[0])
            sublista.append(coluna[1])
            sublista.append(coluna[3])
            lista.append(sublista)
        	    
    return lista