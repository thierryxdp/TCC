def busca(setor, matriz):
    nlinhas = len(matriz)
    ninforcao = len(matriz[0])
    i = 0
    lista = []
    
    while i < nlinhas:
        info_pessoa = matriz[i]
        if info_pessoa[2] == setor:
            info_pessoa.remove(setor)
            lista = lista + [info_pessoa]
        i = i + 1
        
    return lista