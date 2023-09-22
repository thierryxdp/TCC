def busca(setor,matriz):
    lista_busca=[]
    for linha in matriz:
        if linha[2]==setor:
            del(linha[2])
            lista_busca.append(linha)
    return lista_busca