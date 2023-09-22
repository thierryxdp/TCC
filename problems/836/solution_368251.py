def busca(setor,matriz):
    """Esta função recebe uma lista n x 4 sómente de strings e  uma palavra que deve ser igual a da 3 terceira da linha que você quiser ter a informação e retorna todas as linhas que tem na coluna 3 a string que foi dada na entrada 
    str, list -> list"""
    c = 0
    lista = []
    while c < len(matriz):
        if setor == matriz[c][2]:
            lista.append(matriz[c])
            del matriz[c][2]
    	c += 1
    return lista