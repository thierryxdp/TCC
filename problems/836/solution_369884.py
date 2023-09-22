def busca(setor, matriz):
    
    lista_setor = []
    for lin in matriz:
        if lin[2] == setor:
            lista_setor.append(lin)
    return lista_setor